"""
Currency.

---
layout:     post
source:     SublimeLinter-annotations
source_url: http://bit.ly/16Q7H41
title:      symbols
date:       2014-06-10 12:31:19
categories: writing
---

Currency symbols.

"""

from proselint.registry.checks import Check, Padding, types

check = Check(
    check_type=types.Existence(
        items=(r"\$[\d]* ?(?:dollars|usd|us dollars)",),
        padding=Padding.SEPARATOR_IN_TEXT,
    ),
    path="misc.currency",
    message="Incorrect use of symbols in {}.",
)

__register__ = (check,)
