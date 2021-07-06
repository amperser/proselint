# -*- coding: utf-8 -*-
u"""a.m. / p.m.

---
layout:     post
source:     Garner's Modern American Usage
source_url: http://bit.ly/1T4alrY
title:      a.m. & p.m.
date:       2014-06-10 12:31:19
categories: writing
---

"""
from proselint.tools import memoize, existence_check


@memoize
def check_lowercase_periods(text):
    """Check the text."""
    err = "dates_times.am_pm.lowercase_periods"
    msg = u"With lowercase letters, the periods are standard."

    return existence_check(text, [r"\d{1,2} ?[ap]m"], err, msg)


@memoize
def check_spacing(text):
    """Check the text."""
    err = "dates_times.am_pm.spacing"
    msg = u"It's standard to put a space before 'a.m.' or 'p.m.'."

    return existence_check(text, [r"\d{1,2}[ap]\.?m\.?"], err, msg)


@memoize
def check_midnight_noon(text):
    """Check the text."""
    err = "dates_times.am_pm.midnight_noon"
    msg = (u"12 a.m. and 12 p.m. are wrong and confusing."
           " Use 'midnight' or 'noon'.")

    return existence_check(text, [r"12 ?[ap]\.?m\.?"], err, msg)


@memoize
def check_redundancy(text):
    """Check the text."""
    err = "dates_times.am_pm.midnight_noon"
    msg = (u"'a.m.' is always morning; 'p.m.' is always night.")

    list = [
        r"\d{1,2} ?a\.?m\.? in the morning",
        r"\d{1,2} ?p\.?m\.? in the evening",
        r"\d{1,2} ?p\.?m\.? at night",
        r"\d{1,2} ?p\.?m\.? in the afternoon",
    ]

    return existence_check(text, list, err, msg, join=True)
