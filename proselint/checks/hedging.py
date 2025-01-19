"""
Hedging.

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

from proselint.checks import CheckSpec, Existence

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "I would argue that this is a good test.",
    "You could say that, so to speak.",
]

check = CheckSpec(
    Existence([
        "I would argue that",
        "so to speak",
        "to a certain degree",
    ]),
    "hedging.misc",
    "Hedging. Just say it.",
)

__register__ = (check,)
