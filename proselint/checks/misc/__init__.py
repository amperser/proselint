"""Miscellaneous advice not otherwise categorized."""
# TODO: why are these not in _root of check-dir?

from proselint.checks.misc.apologizing import (
    __register__ as register_apologizing,
)
from proselint.checks.misc.back_formations import (
    __register__ as register_back_formations,
)
from proselint.checks.misc.braces import __register__ as register_braces
from proselint.checks.misc.bureaucratese import (
    __register__ as register_bureaucratese,
)
from proselint.checks.misc.but import __register__ as register_but
from proselint.checks.misc.capitalization import (
    __register__ as register_capitalization,
)
from proselint.checks.misc.chatspeak import __register__ as register_chatspeak
from proselint.checks.misc.commercialese import (
    __register__ as register_commercialese,
)
from proselint.checks.misc.composition import (
    __register__ as register_composition,
)
from proselint.checks.misc.currency import __register__ as register_currency
from proselint.checks.misc.debased import __register__ as register_debased
from proselint.checks.misc.greylist import __register__ as register_greylist
from proselint.checks.misc.illogic import __register__ as register_illogic
from proselint.checks.misc.inferior_superior import (
    __register__ as register_inferior_superior,
)
from proselint.checks.misc.institution_name import (
    __register__ as register_institution_name,
)
from proselint.checks.misc.latin import __register__ as register_latin
from proselint.checks.misc.many_a import __register__ as register_many_a
from proselint.checks.misc.metadiscourse import (
    __register__ as register_metadiscourse,
)
from proselint.checks.misc.monotonic import __register__ as register_monotonic
from proselint.checks.misc.narcissism import (
    __register__ as register_narcissism,
)
from proselint.checks.misc.not_guilty import (
    __register__ as register_not_guilty,
)
from proselint.checks.misc.numbers import __register__ as register_numbers
from proselint.checks.misc.phrasal_adjectives import (
    __register__ as register_phrasal_adjectives,
)
from proselint.checks.misc.plurals import __register__ as register_plurals
from proselint.checks.misc.preferred_forms import (
    __register__ as register_preferred_forms,
)
from proselint.checks.misc.pretension import (
    __register__ as register_pretension,
)
from proselint.checks.misc.professions import (
    __register__ as register_professions,
)
from proselint.checks.misc.scare_quotes import (
    __register__ as register_scare_quotes,
)
from proselint.checks.misc.suddenly import __register__ as register_suddenly
from proselint.checks.misc.tense_present import (
    __register__ as register_tense_present,
)
from proselint.checks.misc.waxed import __register__ as register_waxed
from proselint.checks.misc.whence import __register__ as register_whence

__register__ = (
    *register_apologizing,
    *register_back_formations,
    *register_braces,
    *register_bureaucratese,
    *register_but,
    *register_capitalization,
    *register_chatspeak,
    *register_commercialese,
    *register_composition,
    *register_currency,
    *register_debased,
    *register_greylist,
    *register_illogic,
    *register_inferior_superior,
    *register_institution_name,
    *register_latin,
    *register_many_a,
    *register_metadiscourse,
    *register_monotonic,
    *register_narcissism,
    *register_not_guilty,
    *register_numbers,
    *register_phrasal_adjectives,
    *register_plurals,
    *register_preferred_forms,
    *register_pretension,
    *register_professions,
    *register_scare_quotes,
    *register_suddenly,
    *register_tense_present,
    *register_waxed,
    *register_whence,
)
