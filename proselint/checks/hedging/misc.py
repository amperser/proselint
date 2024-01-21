"""Hedging.

---
layout:     post
source:     Pinker's book on writing
source_url: ???
title:      hedging
date:       2014-06-10
categories: writing
---

Points out hedging.

"""
from __future__ import annotations

from proselint.checks import ResultCheck
from proselint.checks import existence_check

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "I would argue that this is a good test.",
    "You could say that, so to speak.",
]


def check(text: str) -> list[ResultCheck]:
    """Suggest the preferred forms."""
    err = "hedging.misc"
    msg = "Hedging. Just say it."

    narcissism = [
        "I would argue that",
        "so to speak",
        "to a certain degree",
    ]

    return existence_check(text, narcissism, err, msg)
