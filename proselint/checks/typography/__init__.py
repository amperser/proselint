"""Advice on typography."""

from proselint.checks.typography import (
    diacritical_marks,
    spacing,
    symbols,
)

__register__ = (
    *diacritical_marks.__register__,
    *spacing.__register__,
    *symbols.__register__,
)
