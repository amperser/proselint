"""Dates and times."""

from proselint.checks.dates_times import am_pm, dates

__register__ = (
    *am_pm.__register__,
    *dates.__register__,
)
