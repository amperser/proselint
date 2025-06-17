"""Weasel words."""

from proselint.registry import build_modules_register

__register__ = build_modules_register(
    (".misc", ".very"),
    "proselint.checks.weasel_words",
)
