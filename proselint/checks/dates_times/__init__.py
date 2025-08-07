"""Dates and times."""

from proselint.registry import build_modules_register

__register__ = build_modules_register(
    (".am_pm", ".dates"),
    "proselint.checks.dates_times",
)
