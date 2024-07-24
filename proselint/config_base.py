"""Proselint config - replacement for default .proselintrc since #1212."""

from __future__ import annotations

from enum import IntEnum
from typing import TypedDict


class Output(IntEnum):
    """Control linter output format."""

    full = default = 0
    json = 1
    compact = 2
    # implement printing to file?

    @classmethod
    def names(cls) -> list[str]:
        """Return the names of output levels."""
        return [_e.name for _e in cls]


class Config(TypedDict):
    """Configuration for proselint."""

    max_errors: int
    parallelize: bool
    output_format: Output
    checks: dict[str, bool]


proselint_base: Config = {
    "max_errors": 1000,
    "parallelize": True,  # NOTE: has overhead, noticeable for small content
    "output_format": Output.compact,
    "checks": {
        "annotations": True,
        "archaism": True,
        "cliches": True,
        "consistency": True,
        "dates_times": True,
        "hedging": True,
        "industrial_language": True,
        "lexical_illusions": True,
        "malapropisms": True,
        "misc": True,
        "misc.monotonic": False,  # in preview phase
        "mixed_metaphors": True,
        "mondegreens": True,
        "needless_variants": True,
        "nonwords": True,
        "oxymorons": True,
        "punctuation": True,
        "redundancy": True,
        "skunked_terms": True,
        "social_awareness": False,  # in preview phase
        "spelling": True,
        "scientific": True,
        "scientific.misc": False,  # in preview phase
        "terms": True,
        "typography": True,
        "uncomparables": True,
        "weasel_words": True,
        "restricted": False,  # restrictive writing styles, off by default
    },
}
