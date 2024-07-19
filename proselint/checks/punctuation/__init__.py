"""Check for puntuation spacing and hyperbole."""

from proselint.checks.punctuation.hyperbole import (
    __register__ as register_hyperbole,
)
from proselint.checks.punctuation.misc import __register__ as register_misc

__register__ = (
    *register_hyperbole,
    *register_misc,
)
