"""Avoid cliches."""

from proselint.checks import CheckRegistry
from proselint.checks.cliches.hell import register_with as register_hell
from proselint.checks.cliches.misc import register_with as register_misc


def register_with(registry: CheckRegistry) -> None:
    """Register the checks."""
    register_hell(registry)
    register_misc(registry)
