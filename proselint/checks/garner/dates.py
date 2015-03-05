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
def check_decade_apostrophes_short(blob):
    """Check the text for dates of the form X0's."""
    err = "MAU103"
    msg = u"Apostrophes aren't needed for decades."

    regex = "\d0\'s"

    return existence_check(
        blob, [regex], err, msg, excluded_topics=["50 Cent"])


@memoize
def check_decade_apostrophes_long(blob):
    """Check the text for dates of the form XXX0's."""
    err = "MAU103"
    msg = u"Apostrophes aren't needed for decades."

    regex = "\d\d\d0\'s"
    return existence_check(blob, [regex], err, msg)


@memoize
def check_dash_and_from(blob):
    """Check the text."""
    err = "MAU103"
    msg = u"When specifying a date range, write 'from X to Y'."

    regex = "from \d+[^ \t\n\r\f\va-zA-Z0-9_]\d+"
    return existence_check(blob, [regex], err, msg)


def check_month_year_comma(blob):
    """Check the text."""
    err = "MAU103"
    msg = u"When specifying a month and year, no comma is needed."

    regex = "(?:" + "|".join(calendar.month_name[1:]) + "), \d{3,}"
    return existence_check(blob, [regex], err, msg)


@memoize
def check_month_of_year(blob):
    """Check the text."""
    err = "MAU103"
    msg = u"When specifying a month and year, 'of' is unnecessary."

    regex = "(?:" + "|".join(calendar.month_name[1:]) + ") of \d{3,}"
    return existence_check(blob, [regex], err, msg)
