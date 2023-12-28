"""Debased language.

---
layout:     post
source:     ???
source_url: ???
title:      yelling
date:       2014-06-10 12:31:19
categories: writing
---

Too much yelling.

"""
from __future__ import annotations

from proselint.tools import ResultCheck, existence_check, memoize


@memoize
def check(text: str) -> list[ResultCheck]:
    """Check the text."""
    err = "misc.debased"
    msg = "Bad usage, debased language, a continuous temptation."

    items = [
        "a not unjustifiable assumption",
        "leaves much to be desired",
        "would serve no purpose",
        "a consideration which we should do well to bear in mind",
    ]

    return existence_check(text, items, err, msg)
