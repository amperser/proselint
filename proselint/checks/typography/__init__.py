"""Advice on typography."""

from proselint.checks import CheckRegistry
from proselint.checks.typography.diacritical_marks import (
    register_with as register_diacritical_marks,
)
from proselint.checks.typography.exclamation import (
    register_with as register_exclamation,
)
from proselint.checks.typography.symbols import (
    register_with as register_symbols,
)


def register_with(registry: CheckRegistry) -> None:
    """Register the check."""
    register_diacritical_marks(registry)
    register_exclamation(registry)
    register_symbols(registry)
