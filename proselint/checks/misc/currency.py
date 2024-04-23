"""Currency.

---
layout:     post
source:     SublimeLinter-annotations
source_url: http://bit.ly/16Q7H41
title:      symbols
date:       2014-06-10
categories: writing
---

Symbols.

"""
from __future__ import annotations

from proselint.checks import Pd
from proselint.checks import CheckResult
from proselint.checks import existence_check

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "It cost $10 dollars.",
]


def check(text: str) -> list[CheckResult]:
    """Check the text."""
    err = "misc.currency"
    msg = "Incorrect use of symbols in {}."

    symbols = [
        r"\$[\d]* ?(?:dollars|usd|us dollars)",
    ]

    return existence_check(text, symbols, err, msg, padding=Pd.sep_in_txt)
