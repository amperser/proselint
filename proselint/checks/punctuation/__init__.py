"""check for puntuation spacing."""

from proselint.checks.punctuation.misc import __register__ as register_misc
from proselint.checks.punctuation.spacing import (
    __register__ as register_spacing,
)

__register__ = (
    *register_misc,
    *register_spacing,
)
