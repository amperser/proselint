"""check for puntuation spacing."""

from proselint.checks import CheckRegistry
from proselint.checks.punctuation.misc import register_with as register_misc
from proselint.checks.punctuation.spacing import (
    register_with as register_spacing,
)


def register_with(registry: CheckRegistry) -> None:
    """Register the checks."""
    register_misc(registry)
    register_spacing(registry)
