"""Restricted word lists."""

from proselint.registry import build_modules_register

__register__ = build_modules_register(
    (".elementary", ".top1000"),
    "proselint.checks.restricted",
)
