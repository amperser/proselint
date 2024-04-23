"""On 'the N word'.

---
layout:     post
source:     Louis CK
source_url: https://youtu.be/dF1NUposXVQ?t=30s
title:      the 'n-word'
date:       2014-06-10
categories: writing
---

Take responsibility with the shitty words you wanna say.

"""
from __future__ import annotations

from proselint.checks import CheckResult
from proselint.checks import existence_check

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "Have i used the n-word?",
]


def check(text: str) -> list[CheckResult]:
    """Check the text."""
    err = "cursing.nword"
    msg = "Take responsibility for the shitty words you want to say."

    items = [
        "the n-word",
    ]

    return existence_check(text, items, err, msg)
