"""Restricted word lists."""

from proselint.checks import CheckRegistry
from proselint.checks.restricted.elementary import (
    register_with as register_elementary,
)
from proselint.checks.restricted.top1000 import (
    register_with as register_top1000,
)


def register_with(registry: CheckRegistry) -> None:
    """Register the checks."""
    register_elementary(registry)
    register_top1000(registry)
