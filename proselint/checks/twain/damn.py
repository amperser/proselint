# -*- coding: utf-8 -*-
"""Very.

---
layout:     post
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
def check_very_damn(text):
    """Use the registered trademark symbol instead of (R)."""
    err = "twain.damn"
    msg = ("Substitute 'damn' every time you're "
           "inclined to write 'very;' your editor will delete it "
           "and the writing will be just as it should be.")
    regex = "very"

    return existence_check(text, [regex], err, msg, max_errors=1)
