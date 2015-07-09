# -*- coding: utf-8 -*-
"""Pretension.

---
layout:     post
source:     ???
source_url: ???
title:      yelling
date:       2014-06-10 12:31:19
categories: writing
---

Never use the phrase 'all hell broke loose'.

"""
from tools import existence_check, memoize


@memoize
def check_repeated_exclamations(text):
    """Check the text."""
    err = "ogilvy.pretension"
    msg = u"Jargon words like this one are the hallmarks of a pretentious ass."

    list = [
        "reconceptualize",
        "demassification",
        "attitudinally",
        "judgmentally",
    ]

    return existence_check(text, list, err, msg, max_errors=1)
