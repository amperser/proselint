# -*- coding: utf-8 -*-
"""Punctuation.

---
layout:     post
source:     Garner's Modern American Usage
source_url: http://amzn.to/15wF76r
title:      dates
date:       2014-06-10 12:31:19
categories: writing
---

Dates.

"""
from tools import existence_check, memoize


@memoize
def check_et_al(text):
    """Check the text."""
    err = "garner.punctuation"
    msg = u"Misplaced punctuation. It's 'et al.'"

    list = [
        "et. al",
        "et. al."
    ]
    return existence_check(text, list, err, msg, join=True)
