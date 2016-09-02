# -*- coding: utf-8 -*-
"""Skunked terms.

---
layout:     post
source:     Garner's Modern American Usage
source_url: http://bit.ly/1T4alrY
title:      Skunked terms.
date:       2014-06-10 12:31:19
categories: writing
---

Archaism.

"""
from proselint.tools import existence_check, memoize


@memoize
def check(text):
    """Check the text."""
    err = "skunked_terms.misc"
    msg = u"""'{}' is a bit of a skunked term — impossible to use without issue.
             Find some other way to say it."""

    skunked_terms = [
        "bona fides",
        "deceptively",
        "decimate",
        "effete",
        "fulsome",
        "hopefully",
        "impassionate",
        "Thankfully,",
    ]

    return existence_check(text, skunked_terms, err, msg)
