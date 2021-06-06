# -*- coding: utf-8 -*-

"""Mixed metaphors.

---
layout:     post
source:     Garner's Modern American Usage
source_url: http://bit.ly/1T4alrY
title:      ????????
date:       ????????
categories: writing
---

Avoid mixing metaphors.

"""

from proselint.tools import memoize, preferred_forms_check


@memoize
def check(text):
    """Avoid mixing metaphors.

    """
    err = "mixed_metaphors.misc"
    msg = u"Mixed metaphor. Try '{}'."

    list = [
        ["cream rises to the top",    ["cream rises to the crop"]],
        ["fasten your seatbelts",     ["button your seatbelts"]],
        ["a minute to decompress",    ["a minute to decompose"]],
        ["sharpest tool in the shed", ["sharpest marble in the (shed|box)"]],
        ["not rocket science",        ["not rocket surgery"]],
    ]

    return preferred_forms_check(text, list, err, msg)
