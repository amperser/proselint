"""Miscellaneous advice not otherwise categorized."""
# TODO: why are these not in _root of check-dir?

from proselint.checks import CheckRegistry
from proselint.checks.misc.apologizing import (
    register_with as register_apologizing,
)
from proselint.checks.misc.back_formations import (
    register_with as register_back_formations,
)
from proselint.checks.misc.braces import register_with as register_braces
from proselint.checks.misc.bureaucratese import (
    register_with as register_bureaucratese,
)
from proselint.checks.misc.but import register_with as register_but
from proselint.checks.misc.capitalization import (
    register_with as register_capitalization,
)
from proselint.checks.misc.chatspeak import register_with as register_chatspeak
from proselint.checks.misc.commercialese import (
    register_with as register_commercialese,
)
from proselint.checks.misc.composition import (
    register_with as register_composition,
)
from proselint.checks.misc.currency import register_with as register_currency
from proselint.checks.misc.debased import register_with as register_debased
from proselint.checks.misc.greylist import register_with as register_greylist
from proselint.checks.misc.illogic import register_with as register_illogic
from proselint.checks.misc.inferior_superior import (
    register_with as register_inferior_superior,
)
from proselint.checks.misc.institution_name import (
    register_with as register_institution_name,
)
from proselint.checks.misc.latin import register_with as register_latin
from proselint.checks.misc.many_a import register_with as register_many_a
from proselint.checks.misc.metadiscourse import (
    register_with as register_metadiscourse,
)
from proselint.checks.misc.monotonic import register_with as register_monotonic
from proselint.checks.misc.narcissism import (
    register_with as register_narcissism,
)
from proselint.checks.misc.not_guilty import (
    register_with as register_not_guilty,
)
from proselint.checks.misc.numbers import register_with as register_numbers
from proselint.checks.misc.phrasal_adjectives import (
    register_with as register_phrasal_adjectives,
)
from proselint.checks.misc.plurals import register_with as register_plurals
from proselint.checks.misc.preferred_forms import (
    register_with as register_preferred_forms,
)
from proselint.checks.misc.pretension import (
    register_with as register_pretension,
)
from proselint.checks.misc.professions import (
    register_with as register_professions,
)
from proselint.checks.misc.scare_quotes import (
    register_with as register_scare_quotes,
)
from proselint.checks.misc.suddenly import register_with as register_suddenly
from proselint.checks.misc.tense_present import (
    register_with as register_tense_present,
)
from proselint.checks.misc.waxed import register_with as register_waxed
from proselint.checks.misc.whence import register_with as register_whence


def register_with(registry: CheckRegistry) -> None:
    """Register the checks."""
    register_apologizing(registry)
    register_back_formations(registry)
    register_braces(registry)
    register_bureaucratese(registry)
    register_but(registry)
    register_capitalization(registry)
    register_chatspeak(registry)
    register_commercialese(registry)
    register_composition(registry)
    register_currency(registry)
    register_debased(registry)
    register_greylist(registry)
    register_illogic(registry)
    register_inferior_superior(registry)
    register_institution_name(registry)
    register_latin(registry)
    register_many_a(registry)
    register_metadiscourse(registry)
    register_monotonic(registry)
    register_narcissism(registry)
    register_not_guilty(registry)
    register_numbers(registry)
    register_phrasal_adjectives(registry)
    register_plurals(registry)
    register_preferred_forms(registry)
    register_pretension(registry)
    register_professions(registry)
    register_scare_quotes(registry)
    register_suddenly(registry)
    register_tense_present(registry)
    register_waxed(registry)
    register_whence(registry)
