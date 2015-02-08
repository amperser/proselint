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
from proselint.tools import blacklist, memoize


@memoize
def check(text):

    err = "MAU108"
    msg = u"'{}' is airlinese."

    airlinese = [
        "enplan(?:e|ed|ing|ement)",
        "momentarily",
    ]

    return blacklist(text, airlinese, err, msg)
