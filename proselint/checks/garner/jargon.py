# -*- coding: utf-8 -*-
u"""MAU100: Cliches.

---
layout:     post
error_code: MAU101
source:     Garner's Modern American Usage
source_url: http://amzn.to/15wF76r
title:      a vs. an
date:       2014-06-10 12:31:19
categories: writing
---

Cliches are cliché.

"""
from proselint.tools import memoize, existence_check


@memoize
def check(blob):
    """Check the text."""
    err = "MAU101"
    msg = u"'{}' is jargon. Can you replace it with something more standard?"

    jargon = [
        "in the affirmative",
        "in the negative",
        "agendize",
        "per your order",
        "per your request",
        "disincentivize",
    ]

    return existence_check(blob, jargon, err, msg, join=True)
