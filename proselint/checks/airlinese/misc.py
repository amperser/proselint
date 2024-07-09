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

from proselint.checks import CheckResult, existence_check, registry

examples_pass = [
    "Smoke phrase with nothing flagged.",
    "Have I menplaned that?",
]

examples_fail = [
    "We getting all deplaned.",
]


def check(text: str) -> list[CheckResult]:
    """Check the text."""
    err = "airlinese.misc"
    msg = "'{}' is airlinese."

    airlinese = [
        "enplan(?:e|ed|ing|ement)",
        "deplan(?:e|ed|ing|ement)",
        "taking off momentarily",
    ]

    return existence_check(text, airlinese, err, msg)


registry.register("airlinese.misc", check)
