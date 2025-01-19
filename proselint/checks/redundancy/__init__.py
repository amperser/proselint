"""Redundancy."""

from proselint.checks.redundancy import misc, ras_syndrome

__register__ = (
    *misc.__register__,
    *ras_syndrome.__register__,
)
