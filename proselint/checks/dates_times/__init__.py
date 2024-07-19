"""Dates and times."""

from proselint.checks.dates_times.am_pm import __register__ as register_am_pm
from proselint.checks.dates_times.dates import __register__ as register_dates

__register__ = (
    *register_am_pm,
    *register_dates,
)
