"""
Bureaucratese.

---
layout:     post
source:     Garner's Modern American Usage
source_url: http://bit.ly/1T4alrY
title:      bureaucratese
date:       2014-06-10
categories: writing
---

Bureaucratese.

"""
from __future__ import annotations

from proselint.checks import CheckResult, existence_check

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "I hope the report meets with your approval.",
]


def check(text: str) -> list[CheckResult]:
    """Check the text."""
    err = "misc.bureaucratese"
    msg = "'{}' is bureaucratese."

    bureaucratese = [
        "meet with your approval",
        "meets with your approval",
    ]

    return existence_check(text, bureaucratese, err, msg)
