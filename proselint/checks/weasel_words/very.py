# -*- coding: utf-8 -*-
"""Very.

---
layout:     post
source:     William Allen White
source_url: http://bit.ly/1XaMllw
title:      very
date:       2014-06-10 12:31:19
categories: writing
---

Substitute 'damn' every time you're inclined to write 'very'; your editor will
delete it and the writing will be just as it should be.

"""
from proselint.tools import memoize, existence_check


@memoize
def check(text):
    """Avoid 'very'."""
    err = "weasel_words.very"
    msg = ("Substitute 'damn' every time you're "
           "inclined to write 'very'; your editor will delete it "
           "and the writing will be just as it should be.")
    regex = "very"

    return existence_check(text, [regex], err, msg, max_errors=1)
