"""Restricted word lists."""

from proselint.checks.restricted.elementary import (
    __register__ as register_elementary,
)
from proselint.checks.restricted.top1000 import (
    __register__ as register_top1000,
)

__register__ = (
    *register_elementary,
    *register_top1000,
)
