# -*- coding: utf-8 -*-
"""EES: Too much yelling.

---
layout:     post
error_code: SCH
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
def check_repeated_exclamations(blob):
    """Check the text."""
    err = "leonard.hell"
    msg = u"Never use the words 'all hell broke loose'."

    regex = r"all hell broke loose"

    return existence_check(
        blob, [regex], err, msg, max_errors=1)
