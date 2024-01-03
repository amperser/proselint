"""Dates.

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
from __future__ import annotations

import calendar

from ...lint_checks import ResultCheck, existence_check


def check_decade_apostrophes_short(text: str) -> list[ResultCheck]:
    """Check the text for dates of the form X0's."""
    err = "dates_times.dates"
    msg = "Apostrophes aren't needed for decades."
    items = [r"\d0\'s"]
    return existence_check(text, items, err, msg, excluded_topics=["50 Cent"])


def check_decade_apostrophes_long(text: str) -> list[ResultCheck]:
    """Check the text for dates of the form XXX0's."""
    err = "dates_times.dates"
    msg = "Apostrophes aren't needed for decades."
    items = [r"\d\d\d0\'s"]
    return existence_check(text, items, err, msg)


def check_dash_and_from(text: str) -> list[ResultCheck]:
    """Check the text."""
    err = "dates_times.dates"
    msg = "When specifying a date range, write 'from X to Y'."
    items = [r"[fF]rom \d+[^ \t\n\r\f\va-zA-Z0-9_\.]\d+"]
    return existence_check(text, items, err, msg)


def check_month_year_comma(text: str) -> list[ResultCheck]:
    """Check the text."""
    err = "dates_times.dates"
    msg = "When specifying a month and year, no comma is needed."
    items = [r"(?:" + "|".join(calendar.month_name[1:]) + r"), \d{3,}"]
    return existence_check(text, items, err, msg)


def check_month_of_year(text: str) -> list[ResultCheck]:
    """Check the text."""
    err = "dates_times.dates"
    msg = "When specifying a month and year, 'of' is unnecessary."
    items = [r"(?:" + "|".join(calendar.month_name[1:]) + r") of \d{3,}"]
    return existence_check(text, items, err, msg)
