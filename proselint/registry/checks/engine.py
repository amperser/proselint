# pyright: reportPrivateUsage=false
# ruff: noqa: SLF001
"""Wrap RE2 and re into a unified layer."""

from __future__ import annotations

import re
from enum import IntEnum
from functools import cache
from re import RegexFlag
from typing import TYPE_CHECKING, NamedTuple, TypeAlias

import re2
from re2 import Options

if TYPE_CHECKING:
    from collections.abc import Iterator

Pattern: TypeAlias = "re.Pattern[str] | re2._Regexp[str]"
Match: TypeAlias = "re.Match[str] | re2._Match[str]"


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


class Engine(IntEnum):
    """Which Regex engine to use (RE2 and re respectively)."""

    STANDARD = 0
    FANCY = 1


class RegexOptions(NamedTuple):
    """Options for the Regex `Engine`."""

    case_insensitive: bool = True
    multi_line: bool = False

    @property
    def re_flag(self) -> int | RegexFlag:
        """Return an `RegexFlag` corresponding to the set options."""
        return (int(self.case_insensitive) and RegexFlag.IGNORECASE) | (
            int(self.multi_line) and RegexFlag.MULTILINE
        )

    @property
    def re2_opts(self) -> Options:
        """Return an `Options` corresponding to the set options."""
        opts = Options()
        # TODO: cache static options instead of creating many new objects
        opts.perl_classes = True
        opts.word_boundary = True
        # TODO: opts.never_capture?
        opts.case_sensitive = not self.case_insensitive
        opts.one_line = not self.multi_line
        return opts

    def for_engine(self, engine: Engine) -> int | re.RegexFlag | re2.Options:
        """Return the corresponding options structure for a given engine."""
        if engine == Engine.FANCY:
            return self.re_flag
        return self.re2_opts


class Matcher(NamedTuple):
    """Match patterns in text with a given backend and options."""

    engine: Engine = Engine.STANDARD
    opts: RegexOptions = RegexOptions()

    @cache
    @staticmethod
    def _compiled_pattern_re(
        opts: RegexOptions, pattern: str
    ) -> re.Pattern[str]:
        return re.compile(pattern, opts.re_flag)

    @cache
    @staticmethod
    def _compiled_pattern_re2(
        opts: RegexOptions, pattern: str
    ) -> re2._Regexp[str]:
        return re2.compile(pattern, opts.re2_opts)

    def compiled_pattern_re(self, pattern: str) -> re.Pattern[str]:
        """Compile and cache a `Pattern` with the given options."""
        return Matcher._compiled_pattern_re(self.opts, pattern)

    def compiled_pattern_re2(self, pattern: str) -> re2._Regexp[str]:
        """Compile and cache an `re2._Regexp` with the given options."""
        return Matcher._compiled_pattern_re2(self.opts, pattern)

    def compiled_pattern(self, pattern: str) -> Pattern:
        """Compile and cache a pattern with the given options."""
        return (
            self.compiled_pattern_re2
            if self.engine == Engine.STANDARD
            else self.compiled_pattern_re
        )(pattern)

    def finditer(self, pattern: str, text: str) -> Iterator[Match]:
        """Compile and cache a pattern, then iterate over matches in `text`."""
        return self.compiled_pattern(pattern).finditer(text)

    def search(self, pattern: str, text: str) -> Match | None:
        """Compile and cache a pattern, then find a match in `text`."""
        return self.compiled_pattern(pattern).search(text)

    def fullmatch(self, pattern: str, text: str) -> Match | None:
        """Compile and cache a pattern, then attempt to match `text` wholly."""
        return self.compiled_pattern(pattern).fullmatch(text)

    def exists_in(self, pattern: str, text: str) -> bool:
        """Compile and cache a pattern, then determine if the text matches."""
        return len(pattern) > 0 and self.search(pattern, text) is not None
