# -*- coding: utf-8 -*-
"""Illogic.

---
layout:     post
source:     Garner's Modern American Usage
source_url: http://bit.ly/1T4alrY
title:      Illogic
date:       2014-06-10 12:31:19
categories: writing
---

Archaism.

"""
from proselint.tools import existence_check, memoize


@memoize
def check(text):
    """Check the text."""
    err = "misc.illogic"
    msg = u"'{}' is illogical."

    illogics = [
        "preplan",
        "more than .{1,10} all",
        "appraisal valuations?",
        "(?:i|you|he|she|it|y'all|all y'all|you all|they) could care less",
        "least worst",
        "much-needed gaps?",
        "much-needed voids?",
        "no longer requires oxygen",
        "without scarcely",
    ]

    return existence_check(text, illogics, err, msg, offset=1)


@memoize
def check_coin_a_phrase_from(text):
    """Check the text."""
    err = "misc.illogic.coin"
    msg = "You can't coin an existing phrase. Did you mean 'borrow'?"

    regex = "to coin a phrase from"

    return existence_check(text, [regex], err, msg, offset=1)


@memoize
def check_without_your_collusion(text):
    """Check the textself."""
    err = "misc.illogic.collusion"
    msg = "It's impossible to defraud yourself. Try 'aquiescence'."

    regex = "without your collusion"

    return existence_check(
        text, [regex], err, msg, require_padding=False, offset=-1)
