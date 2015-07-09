# -*- coding: utf-8 -*-
u"""Cliches.

---
layout:     post
source:     Garner's Modern American Usage
source_url: http://amzn.to/15wF76r
title:      a vs. an
date:       2014-06-10 12:31:19
categories: writing
---

Cliches are cliché.

"""
from tools import memoize, existence_check


@memoize
def check(text):
    """Check the text."""
    err = "garner.jargon"
    msg = u"'{}' is jargon. Can you replace it with something more standard?"

    jargon = [
        "in the affirmative",
        "in the negative",
        "agendize",
        "per your order",
        "per your request",
        "disincentivize",
    ]

    return existence_check(text, jargon, err, msg, join=True)
