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
from proselint.tools import existence_check, memoize


@memoize
def check(text):
    """Check the text."""
    err = "misc.currency"
    msg = "Incorrect use of symbols in {}."

    symbols = [
        r"\$[\d]* ?(?:dollars|usd|us dollars)"
    ]

    return existence_check(text, symbols, err, msg)
