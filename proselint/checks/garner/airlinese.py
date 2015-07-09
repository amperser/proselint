# -*- coding: utf-8 -*-
"""Airlinese.

---
layout:     post
source:     Garner's Modern American Usage
source_url: http://amzn.to/15wF76r
title:      Airlinese
date:       2014-06-10 12:31:19
categories: writing
---

Airlinese.

"""
from tools import existence_check, memoize


@memoize
def check(text):
    """Check the text."""
    err = "garner.airlinese"
    msg = u"'{}' is airlinese."

    airlinese = [
        "enplan(?:e|ed|ing|ement)",
        "deplan(?:e|ed|ing|ement)",
        "taking off momentarily",
    ]

    return existence_check(text, airlinese, err, msg)
