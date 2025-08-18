"""Advice on typography."""

from proselint.registry import build_modules_register

__register__ = build_modules_register(
    (".diacritical_marks", ".punctuation", ".symbols"),
    "proselint.checks.typography",
)
