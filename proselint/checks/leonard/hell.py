# -*- coding: utf-8 -*-
"""Too much yelling.

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
    err = "leonard.hell"
    msg = u"Never use the words 'all hell broke loose'."

    regex = r"all hell broke loose"

    return existence_check(
        text, [regex], err, msg, max_errors=1)
