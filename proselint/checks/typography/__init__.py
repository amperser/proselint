"""Advice on typography."""

from proselint.checks.typography.diacritical_marks import (
    __register__ as register_diacritical_marks,
)
from proselint.checks.typography.exclamation import (
    __register__ as register_exclamation,
)
from proselint.checks.typography.symbols import (
    __register__ as register_symbols,
)

__register__ = (
    *register_diacritical_marks,
    *register_exclamation,
    *register_symbols,
)
