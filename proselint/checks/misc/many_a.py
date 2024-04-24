"""
Many a singular.

---
layout:     post
source:     Garner's Modern American Usage
source_url: http://bit.ly/1T4alrY
title:      Many a singular.
date:       2014-06-10
categories: writing
---

The idiom 'many a' requires a singular verb.

"""
from __future__ import annotations

from proselint.checks import CheckResult, preferred_forms_check_opti

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "There were many a day I thought about it.",
]


def check(text: str) -> list[CheckResult]:
    """Suggest the preferred forms."""
    err = "misc.many_a"
    msg = "'many a' requires a singular verb, as in '{}'."

    items: dict[str, str] = {
        "are many a": "is many a",
        "have been many a": "has been many a",
        "were many a": "was many a",
    }

    return preferred_forms_check_opti(text, items, err, msg)
