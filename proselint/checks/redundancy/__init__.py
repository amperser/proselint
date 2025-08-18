"""Redundancy."""

from proselint.registry import build_modules_register

__register__ = build_modules_register(
    (".misc", ".ras_syndrome"),
    "proselint.checks.redundancy",
)
