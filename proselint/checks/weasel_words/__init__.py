"""Weasel words."""

from proselint.checks import CheckRegistry
from proselint.checks.weasel_words.misc import register_with as register_misc
from proselint.checks.weasel_words.very import register_with as register_very


def register_with(registry: CheckRegistry) -> None:
    """Register the checks."""
    register_misc(registry)
    register_very(registry)
