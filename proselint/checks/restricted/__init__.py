"""Restricted word lists."""

from proselint.checks.restricted import elementary, top1000

__register__ = (
    *elementary.__register__,
    *top1000.__register__,
)
