"""Redundancy."""

from proselint.checks import CheckRegistry
from proselint.checks.redundancy.misc import register_with as register_misc
from proselint.checks.redundancy.ras_syndrome import (
    register_with as register_ras_syndrome,
)


def register_with(registry: CheckRegistry) -> None:
    """Register the checks."""
    register_misc(registry)
    register_ras_syndrome(registry)
