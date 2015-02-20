# -*- coding: utf-8 -*-
"""MAU103: Dates.

---
layout:     post
error_code: MAU103
source:     Garner's Modern American Usage
source_url: http://amzn.to/15wF76r
title:      dates
date:       2014-06-10 12:31:19
categories: writing
---

Dates.

"""
from proselint.tools import existence_check, memoize
import calendar


@memoize
def check_decade_apostrophes(text):
    """Check the text."""
    err = "MAU103"
    msg = u"Apostrophes aren't needed for decades."

    regex = "(?:\d\d)?\d0\'s"
    return existence_check(text, [regex], err, msg)


@memoize
def check_dash_and_from(text):
    """Check the text."""
    err = "MAU103"
    msg = u"When specifying a date range, write 'from X to Y'."

    regex = "from \d+[^ \t\n\r\f\va-zA-Z0-9_]\d+",
    return existence_check(text, [regex], err, msg)


@memoize
def check_month_year_comma(text):
    """Check the text."""
    err = "MAU103"
    msg = u"When specifying a month and year, no comma is needed."

    regex = "(?:" + "|".join(calendar.month_name[1:]) + "), \d{3,}",
    return existence_check(text, [regex], err, msg)


@memoize
def check_month_of_year(text):
    """Check the text."""
    err = "MAU103"
    msg = u"When specifying a month and year, 'of' is unnecessary."

    regex = "(?:" + "|".join(calendar.month_name[1:]) + ") of \d{3,}",
    return existence_check(text, [regex], err, msg)
