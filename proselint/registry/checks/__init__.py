"""Check specifications and related options."""

# pyright: reportImportCycles=false

from __future__ import annotations

from collections.abc import Iterator
from enum import Enum
from itertools import chain, islice
from math import ceil
from re import RegexFlag
from typing import TYPE_CHECKING, NamedTuple, Optional

if TYPE_CHECKING:
    from proselint.registry.checks.types import CheckType

BATCH_COUNT = 150
"""The maximum number of entries per batch for splitting larger checks."""


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

    def to_offset_from(self, offset: tuple[int, int]) -> tuple[int, int]:
        """Calculate new offset values based on the applied padding."""
        if self in {Padding.RAW, Padding.SAFE_JOIN, Padding.WORDS_IN_TEXT}:
            return offset
        return (offset[0] + 1, max(offset[1] - 1, 0))


# TODO: use position and span for (line, column) and (start_pos, end_pos)?
class LintResult(NamedTuple):
    """Carry lint result information."""

    check_path: str
    message: str
    line: int
    column: int
    start_pos: int
    end_pos: int
    severity: str
    replacements: Optional[str]

    @property
    def extent(self) -> int:
        """The extent (span width) of the result."""
        return self.end_pos - self.start_pos

    def __str__(self) -> str:  # pyright: ignore[reportImplicitOverride]
        """Convert the `LintResult` into a CLI-suitable format."""
        return f":{self.line}:{self.column}: {self.check_path} {self.message}"


class CheckResult(NamedTuple):
    """Carry check result information."""

    start_pos: int
    end_pos: int
    check_path: str
    message: str
    replacements: Optional[str]


class CheckFlags(NamedTuple):
    """
    Carry applicable check flag settings.

    Currently, this supports:
    - `results_limit`: The maximum number of results to output.
    - `ppm_threshold`: A threshold check comparing the number of results
    against the text length.
    """

    # TODO: it would be more efficient if these could interrupt instead of
    # postprocessing - that is, halt searching if limits are surpassed instead
    # of truncating / alerting if conditions are met after the fact. This may
    # be achieved via iterators instead of working with final lists.
    results_limit: int = 0
    ppm_threshold: int = 0

    @staticmethod
    def truncate(
        results: Iterator[CheckResult], limit: int
    ) -> Iterator[CheckResult]:
        """
        Truncate a list of results to a given threshold.

        This also notes how many times the check flagged prior to truncation.
        """
        if limit == 0:
            return results

        return chain(
            islice(results, limit - 1),
            (
                CheckResult(
                    start_pos=result.start_pos,
                    end_pos=result.end_pos,
                    check_path=result.check_path,
                    message=f"{result.message} Also found elsewhere.",
                    replacements=result.replacements,
                )
                for result in islice(results, 1)
            ),
        )

    @staticmethod
    def apply_threshold(
        results: Iterator[CheckResult], threshold: int, length: int
    ) -> Iterator[CheckResult]:
        """Return an error if the specified PPM `threshold` is surpassed."""
        if 0 in {threshold, length}:
            return results

        req_results = max(ceil((threshold / 1e6) * max(length, 1000)), 2)
        return (
            CheckResult(
                start_pos=result.start_pos,
                end_pos=result.end_pos,
                check_path=result.check_path,
                message=f"{result.message} Surpassed {threshold} ppm.",
                replacements=None,
            )
            for result in islice(results, req_results - 1, req_results)
        )

    def apply(
        self, results: Iterator[CheckResult], text_len: int
    ) -> Iterator[CheckResult]:
        """Apply the specified flags to an iterator of `results`."""
        return CheckFlags.truncate(
            CheckFlags.apply_threshold(results, self.ppm_threshold, text_len),
            self.results_limit,
        )


class Check(NamedTuple):
    """Carry a complete check specification."""

    check_type: CheckType
    path: str = ""
    message: str = ""
    flags: CheckFlags = CheckFlags()
    ignore_case: bool = True
    offset: tuple[int, int] = (0, 0)

    # TODO: for 3.11+, RegexFlag.NOFLAG exists
    @property
    def re_flag(self) -> int:
        """Return a corresponding `RegexFlag` for the `ignore_case` setting."""
        return RegexFlag.IGNORECASE if self.ignore_case else 0

    @property
    def path_segments(self) -> list[str]:
        """Hierarchal segments of the check path."""
        return self.path.split(".")

    def matches_partial(self, partial: str) -> bool:
        """Check if `partial` is a subset key of the full check path."""
        partial_segments = partial.split(".")

        return self.path_segments[:len(partial_segments)] == partial_segments

    def check(self, text: str) -> Iterator[CheckResult]:
        """Apply the check over `text`."""
        return (
            self.check_type
            if callable(self.check_type)
            else self.check_type.check
        )(text, self)

    def check_with_flags(self, text: str) -> Iterator[CheckResult]:
        """Apply the check over `text`, including specified `CheckFlags`."""
        return self.flags.apply(self.check(text), len(text))
