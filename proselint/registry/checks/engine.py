# pyright: reportPrivateUsage=false, reportImplicitOverride=false
# ruff: noqa: SLF001
"""Wrap RE2 and re into a unified layer."""

from __future__ import annotations

import re
from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum, IntEnum
from functools import cache, cached_property
from itertools import chain
from re import RegexFlag
from typing import (
    TYPE_CHECKING,
    Generic,
    TypeAlias,
    TypeVar,
    cast,
)

import re2
from re2 import Options

if TYPE_CHECKING:
    from collections.abc import Collection, Iterator

Pattern: TypeAlias = "re.Pattern[str] | re2._Regexp[str]"
Match: TypeAlias = "re.Match[str] | re2._Match[str]"
PatternSet: TypeAlias = str | re2.Set


class Padding(str, Enum):
    """Regex padding types for checks."""

    RAW = r"{}"
    """Bare text with no padding."""
    SAFE_JOIN = r"(?:{})"
    """Encapsulate patterns in an anonymous group for joining, e.g. x|y|z."""
    WORDS_IN_TEXT = r"\b{}\b"
    """
    Match word position boundaries around the pattern.

    This matches any position between a word character and a non-word character
    or position.
    """
    NONWORDS_IN_TEXT = r"\B{}\B"
    """Match any position that is not a word boundary around the pattern."""
    STRICT_WORDS_IN_TEXT = r"(?<![A-Za-z'-]){}(?![A-Za-z'-])"
    """Lookaround-based `WORDS_IN_TEXT`, prohibiting hyphens and apostrophes."""

    @staticmethod
    def safe_join(patterns: Collection[str]) -> str:
        """Join a collection of patterns with `Padding.SAFE_JOIN`."""
        return (
            (
                Padding.SAFE_JOIN.format("|".join(patterns))
                if len(patterns) > 1
                else next(iter(patterns))
            )
            if patterns
            else ""
        )


class Anchor(IntEnum):
    """
    Determine where a pattern should match (be anchored) in the text.

    This is `Engine.STANDARD`-exclusive behaviour.
    """

    UNANCHORED = 0
    """Match anywhere in the text."""
    ANCHOR_START = 1
    """Match at the start of the text."""
    ANCHOR_BOTH = 2
    """Match at the start and end of the text."""

    def to_re2_set(self, opts: Options | None = None) -> re2.Set:
        """Create an `re2.Set` with the anchor and given options."""
        match self:
            case Anchor.UNANCHORED:
                return re2.Set.SearchSet(opts)
            case Anchor.ANCHOR_START:
                return re2.Set.MatchSet(opts)
            case Anchor.ANCHOR_BOTH:
                return re2.Set.FullMatchSet(opts)


@dataclass(frozen=True)
class RegexOptions:
    """Options for the Regex `Engine`."""

    case_insensitive: bool = True
    multi_line: bool = False

    @cached_property
    def re_flag(self) -> int | RegexFlag:
        """Return a `RegexFlag` corresponding to the set options."""
        return (int(self.case_insensitive) and RegexFlag.IGNORECASE) | (
            int(self.multi_line) and RegexFlag.MULTILINE
        )

    @cached_property
    def re2_opts(self) -> Options:
        """Return an `Options` corresponding to the set options."""
        opts = Options()
        opts.perl_classes = True
        opts.word_boundary = True
        opts.never_capture = True
        opts.case_sensitive = not self.case_insensitive
        opts.one_line = not self.multi_line
        return opts


class Engine(ABC):
    """Abstract base class for Regex engines."""

    opts: RegexOptions

    def __init__(self, opts: RegexOptions | None = None) -> None:
        """Initialise the engine with the given options."""
        self.opts = opts or RegexOptions()

    @abstractmethod
    def compiled_pattern(self, _pattern: str) -> Pattern:
        """Compile and cache a pattern with the given options."""
        ...

    def finditer(self, pattern: str, text: str) -> Iterator[Match]:
        """Compile and cache a pattern, then iterate over matches in `text`."""
        return self.compiled_pattern(pattern).finditer(text)

    def search(self, pattern: str, text: str) -> Match | None:
        """Compile and cache a pattern, then find the first match in `text`."""
        return self.compiled_pattern(pattern).search(text)

    def fullmatch(self, pattern: str, text: str) -> Match | None:
        """Compile and cache a pattern, then attempt to match `text` wholly."""
        return self.compiled_pattern(pattern).fullmatch(text)

    def exists_in(self, pattern: str, text: str) -> bool:
        """Compile and cache a pattern, then check if it matches in `text`."""
        return len(pattern) > 0 and self.search(pattern, text) is not None

    @abstractmethod
    def make_set(
        self,
        _padding: Padding,
        _patterns: Collection[str],
        _anchor: Anchor = Anchor.UNANCHORED,
    ) -> MatchSet[str | re2.Set]:
        """Create a `MatchSet` with the engine."""
        ...


class Fast(Engine):
    """The standard engine, based on RE2."""

    @cache
    @staticmethod
    def _compiled_pattern(pattern: str, opts: RegexOptions) -> re2._Regexp[str]:
        return re2.compile(pattern, opts.re2_opts)

    def compiled_pattern(self, pattern: str) -> re2._Regexp[str]:
        return Fast._compiled_pattern(pattern, self.opts)

    def make_set(
        self,
        padding: Padding,
        patterns: Collection[str],
        anchor: Anchor = Anchor.UNANCHORED,
    ) -> FastSet:
        return FastSet(self, padding, patterns, anchor)


class Fancy(Engine):
    """
    The fancy engine, based on Python's re.

    Only use this if you need access to features not available in `Fast`, like
    lookarounds and backreferences.
    """

    @cache
    @staticmethod
    def _compiled_pattern(pattern: str, opts: RegexOptions) -> re.Pattern[str]:
        return re.compile(pattern, opts.re_flag)

    def compiled_pattern(self, pattern: str) -> re.Pattern[str]:
        return Fancy._compiled_pattern(pattern, self.opts)

    def make_set(
        self,
        padding: Padding,
        patterns: Collection[str],
        _anchor: Anchor = Anchor.UNANCHORED,
    ) -> FancySet:
        return FancySet(self, padding, patterns)


ST_co = TypeVar("ST_co", bound=str | re2.Set, covariant=True)


class MatchSet(ABC, Generic[ST_co]):
    """Abstract base class for Regex match sets."""

    engine: Engine
    padding: Padding
    _set: ST_co

    # TODO: find a way to expose *which* patterns matched

    @abstractmethod
    def construct_set(self, patterns: Collection[str]) -> ST_co:
        """Construct and cache the set."""
        ...

    @abstractmethod
    def exists_in(self, _text: str) -> bool:
        """Determine whether a match exists in the text."""
        ...

    # TODO: explore possibility of a zipped match set for types.Consistency

    @abstractmethod
    def finditer(self, _text: str) -> Iterator[Match]:
        """Return an iterator over matches in the text."""
        ...


class FastSet(MatchSet[re2.Set]):
    """A match set based on the `Fast` engine."""

    engine: Engine
    padding: Padding
    _anchor: Anchor
    _patterns: tuple[str, ...]
    _set: re2.Set

    @cache
    @staticmethod
    def _construct_set(
        engine: Engine,
        padding: Padding,
        patterns: Collection[str],
        anchor: Anchor = Anchor.UNANCHORED,
    ) -> re2.Set:
        match_set = anchor.to_re2_set(engine.opts.re2_opts)
        for pattern in map(padding.format, patterns):
            _ = match_set.Add(pattern)
        match_set.Compile()
        return match_set

    def construct_set(self, patterns: Collection[str]) -> re2.Set:
        return FastSet._construct_set(
            self.engine, self.padding, patterns, self._anchor
        )

    def __init__(
        self,
        engine: Fast,
        padding: Padding,
        patterns: Collection[str],
        anchor: Anchor = Anchor.UNANCHORED,
    ) -> None:
        """Initialise the match set."""
        self.engine = engine
        self.padding = padding

        self._anchor = anchor
        self._patterns = tuple(patterns)
        self._set = self.construct_set(patterns)

    def exists_in(self, text: str) -> bool:
        return self._set.Match(text) is not None

    def finditer(self, text: str) -> Iterator[Match]:
        set_indices = cast("list[int] | None", self._set.Match(text))
        if set_indices is None:
            return iter(())

        return chain.from_iterable(
            self.engine.finditer(self._patterns[idx], text)
            for idx in set_indices
        )


class FancySet(MatchSet[str]):
    """A match set based on the `Fancy` engine."""

    engine: Engine
    padding: Padding
    _set: str

    @cache
    @staticmethod
    def _construct_set(padding: Padding, patterns: Collection[str]) -> str:
        return padding.format(Padding.safe_join(patterns))

    def construct_set(self, patterns: Collection[str]) -> str:
        return FancySet._construct_set(self.padding, patterns)

    def __init__(
        self, engine: Fancy, padding: Padding, patterns: Collection[str]
    ) -> None:
        """Initialise the match set."""
        self.engine = engine
        self.padding = padding
        self._set = self.construct_set(patterns)

    def exists_in(self, text: str) -> bool:
        return self.engine.exists_in(self._set, text)

    def finditer(self, text: str) -> Iterator[Match]:
        return self.engine.finditer(self._set, text)
