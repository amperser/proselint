# -*- coding: utf-8 -*-
"""Oxymorons.

---
layout:     post
source:     Garner's Modern American Usage
source_url: http://amzn.to/15wF76r
title:      Oxymorons
date:       2014-06-10 12:31:19
categories: writing
---

Archaism.

"""
from tools import existence_check, memoize


@memoize
def check(text):
    """Check the text."""
    err = "garner.oxymorons"
    msg = u"'{}' is an oxymoron."

    oxymorons = [
        "amateur expert",
        "increasingly less",
        "advancing backwards?",
        "alludes explicitly to",
        "explicitly alludes to",
        "totally obsolescent",
        "completely obsolescent",
        "generally always",
        "usually always",
        "increasingly less",
        "build down",
        "conspicuous absence",
        "exact estimate",
        "executive secretary",
        "found missing",
        "intense apathy",
        "mandatory choice",
        "nonworking mother",
        "organized mess",
        # "pretty ugly",
        # "sure bet",
    ]

    return existence_check(text, oxymorons, err, msg, offset=1, join=True)
