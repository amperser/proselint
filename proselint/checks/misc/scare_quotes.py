"""
Misuse of scare quotes.

---
layout:     post
source:     Pinker's book on writing
source_url: ???
title:      misuse of scare quotes
date:       2014-06-10
categories: writing
---

Points out misuse of scare quotes.

"""
from __future__ import annotations

from proselint.checks import CheckResult, Pd, existence_check

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "What was the 'take-home message'?",
]


def check(text: str) -> list[CheckResult]:
    """Suggest the preferred forms."""
    err = "misc.scare_quotes.pinker"
    msg = "Misuse of 'scare quotes'. Delete them."

    items = [
        r"\bthe 'take-home message'\B",
    ]

    return existence_check(text, items, err, msg, padding=Pd.disabled)
