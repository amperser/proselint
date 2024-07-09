"""
Malaproprisms.

---
layout:     post
source:     Garner's Modern American Usage
source_url: http://bit.ly/1T4alrY
title:      Malaproprisms
date:       2014-06-10
categories: writing
---

Archaism.

"""
from __future__ import annotations

from proselint.checks import CheckResult, existence_check, registry

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "Found in the Infinitesimal Universe.",
]


def check(text: str) -> list[CheckResult]:
    """Check the text."""
    err = "malapropisms.misc"
    msg = "'{}' is a malapropism."

    illogics = [
        "the infinitesimal universe",
        "a serial experience",
        "attack my voracity",
    ]

    return existence_check(text, illogics, err, msg)


registry.register("malapropisms.misc", check)
