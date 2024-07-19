"""Advice on typography."""

from proselint.checks.typography.diacritical_marks import (
    __register__ as register_diacritical_marks,
)
from proselint.checks.typography.spacing import (
    __register__ as register_spacing,
)
from proselint.checks.typography.symbols import (
    __register__ as register_symbols,
)

__register__ = (
    *register_diacritical_marks,
    *register_spacing,
    *register_symbols,
)
