"""Cliches.

---
layout:     post
source:     Garner's Modern American Usage
source_url: http://bit.ly/1T4alrY
title:      a vs. an TODO: somehow this title is wrong, original missing
date:       2014-06-10 12:31:19
categories: writing
---

Cliches are cliché.

"""
from __future__ import annotations

from ...lint_checks import ResultCheck, existence_check


def check(text: str) -> list[ResultCheck]:
    """Check the text."""
    err = "jargon.misc"
    msg = "'{}' is jargon. Can you replace it with something more standard?"

    jargon = [
        "in the affirmative",
        "in the negative",
        "agendize",
        "per your order",
        "per your request",
        "disincentivize",
    ]

    return existence_check(text, jargon, err, msg, join=True)
