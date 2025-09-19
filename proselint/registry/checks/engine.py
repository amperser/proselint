# pyright: reportPrivateUsage=false
# ruff: noqa: SLF001
"""Wrap RE2 and re into a unified layer."""

from __future__ import annotations

import re
from abc import ABC, abstractmethod
from enum import Enum, IntEnum
from functools import cache, cached_property
from re import RegexFlag
from typing import TYPE_CHECKING, TypeAlias, override

import re2
from re2 import Options

if TYPE_CHECKING:
    from collections.abc import Collection, Iterator

Pattern: TypeAlias = "re.Pattern[str] | re2._Regexp[str]"
Match: TypeAlias = "re.Match[str] | re2._Match[str]"


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


class RegexOptions:
    """Options for the Regex `Engine`."""

    case_insensitive: bool
    multi_line: bool

    def __init__(
        self, *, case_insensitive: bool = True, multi_line: bool = False
    ) -> None:
        """Set the options."""
        self.case_insensitive = case_insensitive
        self.multi_line = multi_line

    @cached_property
    def re_flag(self) -> int | RegexFlag:
        """Return an `RegexFlag` corresponding to the set options."""
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


class Fast(Engine):
    """The standard engine, based on RE2."""

    @cache
    @staticmethod
    def _compiled_pattern(pattern: str, opts: RegexOptions) -> re2._Regexp[str]:
        return re2.compile(pattern, opts.re2_opts)

    @override
    def compiled_pattern(self, pattern: str) -> re2._Regexp[str]:
        return Fast._compiled_pattern(pattern, self.opts)


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

    @override
    def compiled_pattern(self, pattern: str) -> re.Pattern[str]:
        return Fancy._compiled_pattern(pattern, self.opts)
