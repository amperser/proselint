"""Punctuation.

---
layout:     post
source:     Garner's Modern American Usage
source_url: http://bit.ly/1T4alrY
title:      dates
date:       2014-06-10 12:31:19
categories: writing
---

Dates.

"""
from __future__ import annotations

from ...lint_checks import ResultCheck, existence_check


def check(text: str) -> list[ResultCheck]:
    """Check the text."""
    err = "garner.punctuation"
    msg = "Misplaced punctuation. It's 'et al.'"

    items = [
        "et. al",
        "et. al.",
    ]
    return existence_check(text, items, err, msg, join=True)
