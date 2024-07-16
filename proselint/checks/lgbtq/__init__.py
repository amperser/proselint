"""GLAAD."""

from proselint.checks import CheckRegistry
from proselint.checks.lgbtq.offensive_terms import (
    register_with as register_offensive_terms,
)
from proselint.checks.lgbtq.terms import register_with as register_terms


def register_with(registry: CheckRegistry) -> None:
    """Register the checks."""
    register_offensive_terms(registry)
    register_terms(registry)
