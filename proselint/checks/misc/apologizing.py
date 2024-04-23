"""Excessive apologizing.

---
layout:     post
source:     Pinker's book on writing
source_url: ???
title:      excessive apologizing
date:       2014-06-10
categories: writing
---

Points out excessive apologizing.

"""
from __future__ import annotations

from proselint.checks import CheckResult
from proselint.checks import existence_check

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "To say something more research is needed.",
]


def check(text: str) -> list[CheckResult]:
    """Suggest the preferred forms."""
    err = "misc.apologizing.pinker"
    msg = "Excessive apologizing."

    narcissism = [
        "More research is needed",
    ]

    return existence_check(text, narcissism, err, msg)
