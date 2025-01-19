"""Check for puntuation spacing and hyperbole."""

from proselint.checks.punctuation import hyperbole, misc

__register__ = (
    *hyperbole.__register__,
    *misc.__register__,
)
