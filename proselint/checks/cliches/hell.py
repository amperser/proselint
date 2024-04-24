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

from proselint.checks import CheckResult, existence_check, limit_results

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "I was at xyz and then all hell broke loose again.",
]


@limit_results(1)
def check_repeated_exclamations(text: str) -> list[CheckResult]:
    """Check the text."""
    err = "cliches.hell"
    msg = "Never use the words 'all hell broke loose'."

    items = ["all hell broke loose"]

    return existence_check(text, items, err, msg)
