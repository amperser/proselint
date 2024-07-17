"""
Airlinese.

---
layout:     post
source:     Garner's Modern American Usage
source_url: http://bit.ly/1T4alrY
title:      Airlinese
date:       2014-06-10
categories: writing
---

Airlinese.

"""

from __future__ import annotations

from proselint.checks import CheckSpec, Existence

examples_pass = [
    "Smoke phrase with nothing flagged.",
    "Have I menplaned that?",
]

examples_fail = [
    "We getting all deplaned.",
]

check = CheckSpec(
    Existence([
        "enplan(?:e|ed|ing|ement)",
        "deplan(?:e|ed|ing|ement)",
        "taking off momentarily",
    ]),
    "airlinese.misc",
    "'{}' is airlinese.",
)

__register__ = (check,)
