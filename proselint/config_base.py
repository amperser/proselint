"""Proselint config - replacement for default .proselintrc since #1212."""

from __future__ import annotations

from enum import IntEnum


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


proselint_base: dict = {
    "max_errors": 1000,
    "parallelize": True,  # NOTE: has overhead, noticeable for small content
    "output_format": Output.compact.name,
    "checks": {
        "annotations": True,
        "archaism": True,
        "cliches": True,
        "consistency": True,
        "cursing": True,
        "dates_times": True,
        "hedging": True,
        "hyperbole": True,
        "industrial_language": True,
        "lexical_illusions": True,
        "lgbtq": True,
        "malapropisms": True,
        "misc": True,
        "misc.monotonic": False,  # in preview phase
        "mixed_metaphors": True,
        "mondegreens": True,
        "needless_variants": True,
        "nonwords": True,
        "oxymorons": True,
        "psychology": True,
        "punctuation": True,
        "redundancy": True,
        "skunked_terms": True,
        "spelling": True,
        "scientific.misc": False,  # in preview phase
        "scientific.psychology": True,
        "sexism": True,
        "terms": True,
        "typography": True,
        "uncomparables": True,
        "weasel_words": True,
        "restricted.top1000": False,
        "restricted.elementary": False,
    },
}
