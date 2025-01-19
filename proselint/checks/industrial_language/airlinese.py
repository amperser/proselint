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
    "Did that car just hydroplane?",
    "I know how to operate a planing mill.",
]

examples_fail = [
    "This is your captain speaking. We will be taking off momentarily.",
    "We deplaned promptly after.",
]

check = CheckSpec(
    Existence([
        "enplan(?:e|ed|ing|ement)",
        "deplan(?:e|ed|ing|ement)",
        "taking off momentarily",
    ]),
    "industrial_language.airlinese",
    "'{}' is airlinese.",
)

__register__ = (check,)
