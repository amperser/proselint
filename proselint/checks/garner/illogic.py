# -*- coding: utf-8 -*-
"""MAU108: Illogic.

---
layout:     post
error_code: MAU103
source:     Garner's Modern American Usage
source_url: http://amzn.to/15wF76r
title:      Illogic
date:       2014-06-10 12:31:19
categories: writing
---

Archaism.

"""
from tools import existence_check, memoize


@memoize
def check(blob):
    """Check the text."""
    err = "MAU105"
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

    return existence_check(blob, illogics, err, msg, offset=1)


@memoize
def check_coin_a_phrase_from(blob):
    """Check the text."""
    err = "MAU104"
    msg = "You can't coin an existing phrase. Did you mean 'borrow'?"

    regex = "to coin a phrase from"

    return existence_check(blob, [regex], err, msg, offset=1)


@memoize
def check_without_your_collusion(blob):
    """Check the textself."""
    err = "MAU838"
    msg = "It's impossible to defraud yourself. Try 'aquiescence'."

    regex = "without your collusion"

    return existence_check(
        blob, [regex], err, msg, require_padding=False, offset=-1)
