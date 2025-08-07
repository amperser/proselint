"""Avoid cliches."""

from proselint.registry import build_modules_register

__register__ = build_modules_register(
    (".hell", ".misc"),
    "proselint.checks.cliches",
)
