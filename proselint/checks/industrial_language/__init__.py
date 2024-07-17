"""Industrial language."""

from proselint.checks.industrial_language.airlinese import (
    __register__ as register_airlinese,
)
from proselint.checks.industrial_language.bureaucratese import (
    __register__ as register_bureaucratese,
)
from proselint.checks.industrial_language.chatspeak import (
    __register__ as register_chatspeak,
)
from proselint.checks.industrial_language.commercialese import (
    __register__ as register_commercialese,
)
from proselint.checks.industrial_language.jargon import (
    __register__ as register_jargon,
)

__register__ = (
    *register_airlinese,
    *register_bureaucratese,
    *register_chatspeak,
    *register_commercialese,
    *register_jargon,
)
