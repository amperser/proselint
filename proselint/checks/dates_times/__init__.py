"""Dates and times."""

from proselint.checks import CheckRegistry
from proselint.checks.dates_times.am_pm import register_with as register_am_pm
from proselint.checks.dates_times.am_pm import register_with as register_dates


def register_with(registry: CheckRegistry) -> None:
    """Register the checks."""
    register_am_pm(registry)
    register_dates(registry)
