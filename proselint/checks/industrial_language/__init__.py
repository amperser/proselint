"""Industrial language."""

from proselint.checks.industrial_language import (
    airlinese,
    bureaucratese,
    chatspeak,
    commercialese,
    corporate_speak,
    jargon,
)

__register__ = (
    *airlinese.__register__,
    *bureaucratese.__register__,
    *chatspeak.__register__,
    *commercialese.__register__,
    *corporate_speak.__register__,
    *jargon.__register__,
)
