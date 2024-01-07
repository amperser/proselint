"""Proselint config - replacement for default .proselintrc since #1212."""
from __future__ import annotations

from enum import IntEnum


class Output(IntEnum):
    full = default = 0
    json = 1
    compact = 2
    # implement printing to file?

    @classmethod
    def names(cls) -> list[str]:
        return [_e.name for _e in cls]


proselint_base: dict = {
    "max_errors": 1000,
    "parallelize": True,  # note: has an overhead, noticeable for small content
    # TODO: add disabled force-option for usage as module
    #       can be trouble on windows if used wrong
    "output_format": Output.full.name,
    "checks": {
        "airlinese.misc": True,
        "annotations.misc": True,
        "archaism.misc": True,
        "cliches.hell": True,
        "cliches.misc": True,
        "consistency.spacing": True,
        "consistency.spelling": True,
        "corporate_speak.misc": True,
        "cursing.filth": True,
        "cursing.nfl": False,
        "cursing.nword": True,
        "dates_times.am_pm": True,
        "dates_times.dates": True,
        "hedging.misc": True,
        "hyperbole.misc": True,
        "jargon.misc": True,
        "lexical_illusions.misc": True,
        "lgbtq.offensive_terms": True,
        "lgbtq.terms": True,
        "links.broken": False,
        "malapropisms.misc": True,
        "misc.apologizing": True,
        "misc.back_formations": True,
        "misc.bureaucratese": True,
        "misc.but": True,
        "misc.capitalization": True,
        "misc.chatspeak": True,
        "misc.commercialese": True,
        "misc.composition": True,
        "misc.currency": True,
        "misc.debased": True,
        "misc.false_plurals": True,
        "misc.greylist": True,
        "misc.illogic": True,
        "misc.inferior_superior": True,
        "misc.institution_name": True,
        "misc.latin": True,
        "misc.many_a": True,
        "misc.metadiscourse": True,
        "misc.narcissism": True,
        "misc.not_guilty": True,
        "misc.phrasal_adjectives": True,
        "misc.preferred_forms": True,
        "misc.pretension": True,
        "misc.professions": True,
        "misc.punctuation": True,
        "misc.scare_quotes": True,
        "misc.suddenly": True,
        "misc.tense_present": True,
        "misc.waxed": True,
        "misc.whence": True,
        "mixed_metaphors.misc": True,
        "mondegreens.misc": True,
        "needless_variants.misc": True,
        "nonwords.misc": True,
        "oxymorons.misc": True,
        "psychology.misc": True,
        "punctuation_spacing.misc": True,
        "redundancy.misc": True,
        "redundancy.ras_syndrome": True,
        "skunked_terms.misc": True,
        "spelling.able_atable": True,
        "spelling.able_ible": True,
        "spelling.ally_ly": True,
        "spelling.ance_ence": True,
        "spelling.athletes": True,
        "spelling.ely_ly": True,
        "spelling.em_im_en_in": True,
        "spelling.er_or": True,
        "spelling.in_un": True,
        "spelling.misc": True,
        "spelling.ve_of": True,
        "security.credit_card": True,
        "security.password": True,
        "sexism.misc": True,
        "terms.animal_adjectives": True,
        "terms.denizen_labels": True,
        "terms.eponymous_adjectives": True,
        "terms.venery": True,
        "typography.diacritical_marks": True,
        "typography.exclamation": True,
        "typography.symbols": True,
        "uncomparables.misc": True,
        "weasel_words.misc": True,
        "weasel_words.very": True,
    },
}