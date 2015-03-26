# -*- coding: utf-8 -*-
"""MAU103: Very.

---
layout:     post
error_code: MAU103
source:     Mark Twain
source_url: http://bit.ly/1CQPH61
title:      very
date:       2014-06-10 12:31:19
categories: writing
---

Substitute 'damn' every time you're inclined to write 'very;' your editor will
delete it and the writing will be just as it should be.

"""
from tools import memoize, existence_check


@memoize
def check_very_damn(blob):
    """Use the registered trademark symbol instead of (R)."""
    err = "twain.damn"
    msg = u"""Substitute 'damn' every time you're inclined to write 'very;'
    your editor will delete it and the writing will be just as it should be."""
    regex = "very"

    return existence_check(
        blob, [regex], err, msg, max_errors=2)
