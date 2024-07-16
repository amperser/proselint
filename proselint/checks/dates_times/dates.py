"""
Dates.

---
layout:     post
source:     Garner's Modern American Usage
source_url: http://bit.ly/1T4alrY
title:      dates
date:       2014-06-10
categories: writing
---

Dates.

"""

from __future__ import annotations

import calendar

from proselint.checks import CheckRegistry, CheckSpec, Existence, Pd

examples_pass = [
    "Smoke phrase with nothing flagged.",
    "It happened in the 90s.",
    "It happened in the 1980s.",
    "It happened from 2000 to 2005.",
    "It happened in August 2008.",
    "It happened in August 2008.",
    """Dr. Dre suggested to 50's manager that he look into signing
Eminem to the G-Unit record label.""",
]

examples_fail = [
    "It happened in the 90's.",
    "It happened in the 1980's.",
    "It happened from 2000-2005.",
    "It happened in August, 2008.",
    "It happened in August of 2008.",
    "The 50's were swell."
    "From 1999-2002, Sally served as chair of the committee.",
]

check_decade_apostrophes_short = CheckSpec(
    Existence([r"\d0\'s"]),
    "dates_times.dates.apostrophes",
    "Apostrophes aren't needed for decades.",
)

check_decade_apostrophes_long = CheckSpec(
    Existence([r"\d\d\d0\'s"]),
    "dates_times.dates.apostrophes",
    "Apostrophes aren't needed for decades.",
)

check_dash_and_from = CheckSpec(
    Existence([r"from \d+[^ \t\n\r\f\v\w\.]\d+"]),
    "dates_times.dates.dash_and_from",
    "When specifying a date range, write 'from X to Y'.",
)

check_month_year_comma = CheckSpec(
    Existence(
        # NOTE: strangely month_name[0] is ""
        [r"(?:" + "|".join(calendar.month_name[1:]) + r"), \d{3,}"],
        padding=Pd.disabled,
    ),
    "dates_times.dates.month_year_comma",
    "When specifying a month and year, no comma is needed.",
)

check_month_of_year = CheckSpec(
    Existence(
        # NOTE: strangely month_name[0] is ""
        [r"(?:" + "|".join(calendar.month_name[1:]) + r") of \d{3,}"],
        padding=Pd.disabled,
    ),
    "dates_times.dates",
    "When specifying a month and year, 'of' is unnecessary.",
)


def register_with(registry: CheckRegistry) -> None:
    """Register the checks."""
    registry.register_many((
        check_decade_apostrophes_short,
        check_decade_apostrophes_long,
        check_dash_and_from,
        check_month_year_comma,
        check_month_of_year,
    ))
