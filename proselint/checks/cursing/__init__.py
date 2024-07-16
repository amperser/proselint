"""Cursing."""

from proselint.checks import CheckRegistry
from proselint.checks.cursing.filth import register_with as register_filth
from proselint.checks.cursing.nfl import register_with as register_nfl
from proselint.checks.cursing.nword import register_with as register_nword


def register_with(registry: CheckRegistry) -> None:
    """Register the checks."""
    register_filth(registry)
    register_nfl(registry)
    register_nword(registry)
