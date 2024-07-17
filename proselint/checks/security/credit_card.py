"""
Credit card number printed.

---
layout:     post
source:     ???
source_url: ???
title:      credit card number printed
date:       2014-06-10
categories: writing
---

Credit card number printed.

"""

from __future__ import annotations

from proselint.checks import CheckSpec, Existence

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "My credit card number is 5555555555554444.",
]

check = CheckSpec(
    Existence([
        r"4\d{15}",
        r"5[1-5]\d{14}",
        r"3[4,7]\d{13}",
        r"3[0,6,8]\d{12}",
        r"6011\d{12}",
    ]),
    "security.credit_card",
    "Don't put credit card numbers in plain text.",
)

__register__ = (check,)
