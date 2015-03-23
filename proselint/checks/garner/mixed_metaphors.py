# -*- coding: utf-8 -*-
"""MAU104: Mixed metaphors.

---
layout:     post
error_code: MAU104
source:     Garner's Modern American Usage
source_url: http://amzn.to/15wF76r
title:      mixed metaphors
date:       2014-06-10 12:31:19
categories: writing
---

Archaism.

"""
from proselint.tools import preferred_forms_check, memoize


@memoize
def check(blob):
    """Check the text."""
    err = "MAU104"
    msg = u"Mixed metaphor. Try '{}'."

    preferences = [

        ["cream rises to the top",    ["cream rises to the crop"]],
        ["fasten your seatbelts",     ["button your seatbelts"]],
        ["a minute to decompress",    ["a minute to decompose"]],
        ["sharpest tool in the shed", ["sharpest marble in the (shed|box)"]],
        ["not rocket science",        ["not rocket surgery"]],
    ]

    return preferred_forms_check(blob, preferences, err, msg)
