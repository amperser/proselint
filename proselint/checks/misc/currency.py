# -*- coding: utf-8 -*-
"""Currency.

---
layout:     post
source:     SublimeLinter-annotations
source_url: http://bit.ly/16Q7H41
title:      symbols
date:       2014-06-10 12:31:19
categories: writing
---

Symbols.

"""
from tools import existence_check, memoize


@memoize
def check(text):
    """Check the text."""
    err = "misc.currency"
    msg = u"Incorrect use of symbols in {}."

    symbols = [
        "\$[\d]* ?(?:dollars|usd|us dollars)"
    ]

    return existence_check(text, symbols, err, msg)
