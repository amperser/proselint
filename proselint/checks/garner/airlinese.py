# -*- coding: utf-8 -*-
"""MAU108: Airlinese.

---
layout:     post
error_code: MAU109
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
def check(blob):
    """Check the text."""
    err = "garner.airlinese"
    msg = u"'{}' is airlinese."

    airlinese = [
        "enplan(?:e|ed|ing|ement)",
        "deplan(?:e|ed|ing|ement)",
        "taking off momentarily",
    ]

    return existence_check(blob, airlinese, err, msg)
