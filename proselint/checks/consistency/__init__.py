"""Various consistency checks."""

from proselint.checks import CheckRegistry
from proselint.checks.consistency.spacing import (
    register_with as register_spacing,
)
from proselint.checks.consistency.spelling import (
    register_with as register_spelling,
)


def register_with(registry: CheckRegistry) -> None:
    """Register the checks."""
    register_spacing(registry)
    register_spelling(registry)
