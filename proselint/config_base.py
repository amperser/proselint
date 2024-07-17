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
        "airlinese": True,
        "annotations": True,
        "archaism": True,
        "cliches": True,
        "consistency": True,
        "corporate_speak": True,
        "cursing": True,
        "dates_times": True,
        "hedging": True,
        "hyperbole": True,
        "jargon": True,
        "lexical_illusions": True,
        "lgbtq": True,
        "malapropisms": True,
        "misc.apologizing": True,
        "misc.back_formations": True,
        "misc.bureaucratese": True,
        "misc.braces": True,
        "misc.but": True,
        "misc.capitalization": True,
        "misc.chatspeak": True,
        "misc.commercialese": True,
        "misc.composition": True,
        "misc.currency": True,
        "misc.debased": True,
        "misc.greylist": True,
        "misc.illogic": True,
        "misc.inferior_superior": True,
        "misc.institution_name": True,
        "misc.latin": True,
        "misc.numbers": True,
        "misc.many_a": True,
        "misc.metadiscourse": True,
        "misc.monotonic": False,  # in preview phase
        "misc.narcissism": True,
        "misc.not_guilty": True,
        "misc.phrasal_adjectives": True,
        "misc.plurals": True,
        "misc.preferred_forms": True,
        "misc.pretension": True,
        "misc.professions": True,
        "misc.scare_quotes": True,
        "misc.suddenly": True,
        "misc.tense_present": True,
        "misc.waxed": True,
        "misc.whence": True,
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
        "scientific": False,  # in preview phase
        "sexism": True,
        "terms": True,
        "typography": True,
        "uncomparables": True,
        "weasel_words": True,
        "restricted.top1000": False,
        "restricted.elementary": False,
    },
}
