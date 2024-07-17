"""Redundancy."""

from proselint.checks.redundancy.misc import __register__ as register_misc
from proselint.checks.redundancy.ras_syndrome import (
    __register__ as register_ras_syndrome,
)

__register__ = (
    *register_misc,
    *register_ras_syndrome,
)
