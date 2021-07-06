"""Cliches.

---
layout:     post
source:     Garner's Modern American Usage
source_url: http://bit.ly/1T4alrY
title:      a vs. an
date:       2014-06-10 12:31:19
categories: writing
---

Cliches are cliché.

"""
from proselint.tools import existence_check, memoize


@memoize
def check(text):
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
