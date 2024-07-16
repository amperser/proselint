"""Security."""

from proselint.checks import CheckRegistry
from proselint.checks.security.credit_card import (
    register_with as register_credit_card,
)
from proselint.checks.security.password import (
    register_with as register_password,
)


def register_with(registry: CheckRegistry) -> None:
    """Register the checks."""
    register_credit_card(registry)
    register_password(registry)
