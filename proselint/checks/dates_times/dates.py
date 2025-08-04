"""
Dates.

---
layout:     post
source:     Garner's Modern American Usage
source_url: http://bit.ly/1T4alrY
title:      dates
date:       2014-06-10 12:31:19
categories: writing
---

Dates.

"""

import calendar

from proselint.registry.checks import Check, Padding, types

REGEX_MONTHS = Padding.SAFE_JOIN.format("|".join(calendar.month_name[1:]))

checks_decade_apostrophes = tuple(
    Check(
        check_type=types.ExistenceSimple(pattern=pattern),
        path="dates_times.dates.decade_apostrophes",
        message="Apostrophes aren't needed for decades.",
    )
    for pattern in (r"\d0\'s", r"\d\d\d0\'s")
)

check_dash_and_from = Check(
    check_type=types.ExistenceSimple(pattern=r"from \d+[^ \t\n\r\f\v\w_\.]\d+"),
    path="dates_times.dates.dash_and_from",
    message="When specifying a date range, write 'from X to Y'.",
)

check_month_year_comma = Check(
    check_type=types.ExistenceSimple(pattern=REGEX_MONTHS + r", \d{3,}"),
    path="dates_times.dates.month_year_comma",
    message="When specifying a month and year, no comma is needed.",
)

check_month_of_year = Check(
    check_type=types.ExistenceSimple(pattern=REGEX_MONTHS + r" of \d{3,}"),
    path="dates_times.dates.month_of_year",
    message="When specifying a month and year, 'of' is unnecessary.",
)

__register__ = (
    *checks_decade_apostrophes,
    check_dash_and_from,
    check_month_year_comma,
    check_month_of_year,
)
