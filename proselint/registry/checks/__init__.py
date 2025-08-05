"""Check specifications and related options."""

# pyright: reportImportCycles=false

from __future__ import annotations

from enum import Enum
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
    def truncate(results: list[CheckResult], limit: int) -> list[CheckResult]:
        """
        Truncate a list of results to a given threshold.

        This also notes how many times the check flagged prior to truncation.
        """
        if limit == 0 or (num_results := len(results)) <= limit:
            return results

        last_result = results[limit - 1]
        num_extras = num_results - limit
        last_message = last_result.message + " Found {} elsewhere.".format(
            "once" if num_extras == 1 else f"{num_extras} times"
        )

        return [
            *results[0 : limit - 1],
            CheckResult(
                start_pos=last_result.start_pos,
                end_pos=last_result.end_pos,
                check_path=last_result.check_path,
                message=last_message,
                replacements=None,
            ),
        ]

    @staticmethod
    def apply_threshold(
        results: list[CheckResult], threshold: int, length: int
    ) -> list[CheckResult]:
        """Return an error if the specified PPM `threshold` is surpassed."""
        if threshold == 0 or length == 0 or (num_results := len(results)) < 2:
            return []

        length = max(length, 1000)
        if (ppm := (num_results / length) * 1e6) <= threshold:
            return []
        return [CheckResult(
            start_pos=results[0].start_pos,
            end_pos=results[0].end_pos,
            check_path=results[0].check_path,
            message=results[0].message + f" Reached {ppm:.0f} ppm.",
            replacements=None,
        )]

    def apply(
        self, results: list[CheckResult], text_len: int
    ) -> list[CheckResult]:
        """Apply the specified flags to a list of `results`."""
        return CheckFlags.truncate(
            CheckFlags.apply_threshold(results, self.ppm_threshold, text_len)
            if self.ppm_threshold
            else results,
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
        path_segments = self.path_segments

        return len(partial_segments) <= len(path_segments) and all(
            a == b for a, b in zip(path_segments, partial_segments)
        )

    def check(self, text: str) -> list[CheckResult]:
        """Apply the check over `text`."""
        return (
            self.check_type
            if callable(self.check_type)
            else self.check_type.check
        )(text, self)

    def check_with_flags(self, text: str) -> list[CheckResult]:
        """Apply the check over `text`, including specified `CheckFlags`."""
        return self.flags.apply(self.check(text), len(text))
