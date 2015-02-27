# -*- coding: utf-8 -*-
"""MAU120: Oxymorons.

---
layout:     post
error_code: MAU103
source:     Garner's Modern American Usage
source_url: http://amzn.to/15wF76r
title:      Oxymorons
date:       2014-06-10 12:31:19
categories: writing
---

Archaism.

"""
from proselint.tools import existence_check, memoize


@memoize
def check(text):
    """Check the text."""
    err = "MAU120"
    msg = u"'{}' is an oxymoron."

    oxymorons = [
        "amateur expert",
        "increasingly less",
        "advancing backwards?"
    ]

    return existence_check(text, oxymorons, err, msg, offset=1)
