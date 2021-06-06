# -*- coding: utf-8 -*-

"""Mixed metaphors.

---
layout:     post
source:     Sir Ernest Gowers
source_url: http://bit.ly/1CQPH61
title:      ????????
date:       ????????
categories: writing
---

Avoid mixing metaphors about bottles and their necks.

"""

from proselint.tools import memoize, existence_check

@memoize
def check(text):
    err = "mixed_metaphors.misc.bottleneck"
    msg = u"Mixed metaphor — bottles with big necks are easy to pass through."
    list = [
        r"big(?:gest)? bottleneck",
        r"large(?:st)? bottleneck",
        r"world-?wide bottleneck",
        "huge bottleneck",
        "massive bottleneck",
    ]

    return existence_check(text, list, err, msg, max_errors=1)
