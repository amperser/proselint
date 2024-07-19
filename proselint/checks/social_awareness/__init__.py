"""Social awareness."""

from proselint.checks.social_awareness import (
    lgbtq,
    nword,
    sexism,
)

__register__ = (
    *lgbtq.__register__,
    *nword.__register__,
    *sexism.__register__,
)
