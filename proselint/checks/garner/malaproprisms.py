# -*- coding: utf-8 -*-
"""MAU108: Malaproprisms.

---
layout:     post
error_code: MAU103
source:     Garner's Modern American Usage
source_url: http://amzn.to/15wF76r
title:      Malaproprisms
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
    msg = u"'{}' is a malaproprism."

    illogics = [
        "the infinitesimal universe",
        "a serial experience",
        "attack my voracity",
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
