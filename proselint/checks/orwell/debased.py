# -*- coding: utf-8 -*-
"""Debased language.

---
layout:     post
source:     ???
source_url: ???
title:      yelling
date:       2014-06-10 12:31:19
categories: writing
---

Too much yelling.

"""
from tools import existence_check, memoize


@memoize
def check_debased_language(text):
    """Check the text."""
    err = "orwell.debased"
    msg = u"Bad usage, debased language, a continuous temptation."

    list = [
        "a not unjustifiable assumption",
        "leaves much to be desired",
        "would serve no purpose",
        "a consideration which we should do well to bear in mind",
    ]

    return existence_check(text, list, err, msg)
