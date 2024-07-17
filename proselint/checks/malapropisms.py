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

from proselint.checks import CheckSpec, Existence

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "Found in the Infinitesimal Universe.",
]

check = CheckSpec(
    Existence([
        "the infinitesimal universe",
        "a serial experience",
        "attack my voracity",
    ]),
    "malapropisms.misc",
    "'{}' is a malapropism.",
)

__register__ = (check,)
