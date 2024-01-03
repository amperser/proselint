"""On 'the N word'.

---
layout:     post
source:     Louis CK
source_url: https://youtu.be/dF1NUposXVQ?t=30s
title:      the 'n-word'
date:       2014-06-10 12:31:19
categories: writing
---

Take responsibility with the shitty words you wanna say.

"""
from __future__ import annotations

from ...lint_checks import ResultCheck, existence_check


def check(text: str) -> list[ResultCheck]:
    """Check the text."""
    err = "cursing.nword"
    msg = "Take responsibility for the shitty words you want to say."

    items = [
        "the n-word",
    ]

    return existence_check(text, items, err, msg)
