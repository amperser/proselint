"""Avoid cliches."""

from proselint.checks.cliches import hell, misc

__register__ = (
    *hell.__register__,
    *misc.__register__,
)
