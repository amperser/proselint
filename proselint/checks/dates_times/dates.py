"""Dates.

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

from proselint.checks import Pd
from proselint.checks import CheckResult
from proselint.checks import existence_check

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
    "The 50's were swell." "From 1999-2002, Sally served as chair of the committee.",
]


def check_decade_apostrophes_short(text: str) -> list[CheckResult]:
    """Check the text for dates of the form X0's."""
    err = "dates_times.dates"
    msg = "Apostrophes aren't needed for decades."
    items = [r"\d0\'s"]
    return existence_check(text, items, err, msg, excluded_topics=["50 Cent"])


def check_decade_apostrophes_long(text: str) -> list[CheckResult]:
    """Check the text for dates of the form XXX0's."""
    err = "dates_times.dates"
    msg = "Apostrophes aren't needed for decades."
    items = [r"\d\d\d0\'s"]
    return existence_check(text, items, err, msg)


def check_dash_and_from(text: str) -> list[CheckResult]:
    """Check the text."""
    err = "dates_times.dates"
    msg = "When specifying a date range, write 'from X to Y'."
    items = [r"[fF]rom \d+[^ \t\n\r\f\va-zA-Z0-9_\.]\d+"]
    return existence_check(text, items, err, msg)


def check_month_year_comma(text: str) -> list[CheckResult]:
    """Check the text."""
    err = "dates_times.dates"
    msg = "When specifying a month and year, no comma is needed."
    items = [r"(?:" + "|".join(calendar.month_name[1:]) + r"), \d{3,}"]
    # note: strangely month_name[0] is ""
    return existence_check(text, items, err, msg, padding=Pd.disabled)


def check_month_of_year(text: str) -> list[CheckResult]:
    """Check the text."""
    err = "dates_times.dates"
    msg = "When specifying a month and year, 'of' is unnecessary."
    items = [r"(?:" + "|".join(calendar.month_name[1:]) + r") of \d{3,}"]
    # note: strangely month_name[0] is ""
    return existence_check(text, items, err, msg, padding=Pd.disabled)
