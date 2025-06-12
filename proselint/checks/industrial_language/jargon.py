"""
Jargon.

---
layout:     post
source:     Garner's Modern American Usage
source_url: http://bit.ly/1T4alrY
title:      Jargon
date:       2014-06-10
categories: writing
---



"""

from proselint.tools import existence_check


def check(text):
    """Check the text."""
    err = "industrial_language.jargon"
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
