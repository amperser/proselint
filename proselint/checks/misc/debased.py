"""
Debased language.

---
layout:     post
source:     ???
source_url: ???
title:      yelling
date:       2014-06-10
categories: writing
---

Too much yelling.

"""

from __future__ import annotations

from proselint.checks import CheckSpec, Existence

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "This leaves much to be desired.",
]

check = CheckSpec(
    Existence([
        "a not unjustifiable assumption",
        "leaves much to be desired",
        "would serve no purpose",
        "a consideration which we should do well to bear in mind",
    ]),
    "misc.debased",
    "Debased language is a continuous temptation.",
)

__register__ = (check,)
