"""Check specifications and related options."""

# pyright: reportImportCycles=false

from __future__ import annotations

from itertools import islice
from math import ceil
from typing import TYPE_CHECKING, NamedTuple

from proselint.registry.checks.engine import Engine, Fast, Padding

if TYPE_CHECKING:
    from collections.abc import Iterator

    from proselint.registry.checks.types import CheckType

BATCH_COUNT = 150
"""The maximum number of entries per batch for splitting larger checks."""


class CheckResult(NamedTuple):
    """Carry check result information."""

    check_path: str
    message: str
    span: tuple[int, int]
    replacements: str | None


class CheckFlags(NamedTuple):
    """
    Carry applicable check flag settings.

    Currently, this supports:
    - `ppm_threshold`: A threshold check comparing the number of results
    against the text length.
    """

    ppm_threshold: int = 0
    allow_quotes: bool = False

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
                span=result.span,
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
        return CheckFlags.apply_threshold(results, self.ppm_threshold, text_len)


class Check(NamedTuple):
    """Carry a complete check specification."""

    check_type: CheckType
    engine: Engine = Fast()
    path: str = ""
    message: str = ""
    flags: CheckFlags = CheckFlags()
    offset: tuple[int, int] = (0, 0)

    @property
    def path_segments(self) -> list[str]:
        """Hierarchal segments of the check path."""
        return self.path.split(".")

    def matches_partial(self, partial: str) -> bool:
        """Check if `partial` is a subset key of the full check path."""
        return self.path == partial or self.path.startswith(f"{partial}.")

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


__all__ = ("Check", "CheckFlags", "CheckResult", "Padding")
