# -*- coding: utf-8 -*-
u"""a.m. / p.m.

---
layout:     post
source:     Garner's Modern American Usage
source_url: http://amzn.to/15wF76r
title:      a.m. & p.m.
date:       2014-06-10 12:31:19
categories: writing
---

"""
from tools import memoize, existence_check


@memoize
def check_lowercase_periods(text):
    """Check the text."""
    err = "garner.am_pm.lowercase_periods"
    msg = u"With lowercase letters, the periods are standard."

    return existence_check(text, ["\d{1,2} ?[ap]m"], err, msg)


@memoize
def check_spacing(text):
    """Check the text."""
    err = "garner.am_pm.spacing"
    msg = u"It's standard to put a space before 'a.m.' or 'p.m.'."

    return existence_check(text, ["\d{1,2}[ap]\.?m\.?"], err, msg)


@memoize
def check_midnight_noon(text):
    """Check the text."""
    err = "garner.am_pm.midnight_noon"
    msg = (u"12 a.m. and 12 p.m. are wrong and confusing."
           " Use 'midnight' or 'noon'.")

    return existence_check(text, ["12 ?[ap]\.?m\.?"], err, msg)


@memoize
def check_redundancy(text):
    """Check the text."""
    err = "garner.am_pm.midnight_noon"
    msg = (u"'a.m.' is always morning; 'p.m.' is always night.")

    list = [
        "\d{1,2} ?a\.?m\.? in the morning",
        "\d{1,2} ?p\.?m\.? in the evening",
        "\d{1,2} ?p\.?m\.? at night",
        "\d{1,2} ?p\.?m\.? in the afternoon",
    ]

    return existence_check(text, list, err, msg, join=True)
