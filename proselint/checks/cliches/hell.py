"""
Too much yelling.

---
layout:     post
source:     ???
source_url: ???
title:      yelling
date:       2014-06-10
categories: writing
---

Never use the phrase 'all hell broke loose'.

"""

from __future__ import annotations

from proselint.checks import CheckFlags, CheckSpec, Existence

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "I was at xyz and then all hell broke loose again.",
]

check = CheckSpec(
    Existence(["all hell broke loose"]),
    "cliches.hell",
    "Never use the words 'all hell broke loose'.",
    flags=CheckFlags(limit_results=3),
)

__register__ = (check,)
