"""
Password in plain text.

---
layout:     post
source:     ???
source_url: ???
title:      password in plain text
date:       2014-06-10
categories: writing
---

Don't put pass
"""

from __future__ import annotations

from proselint.checks import CheckSpec, Existence, Pd

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "The password is 123456.",
    "My password is PASSWORD.",
]

_regex = r"[:]? [\S]{6,30}"

check = CheckSpec(
    Existence(
        [
            rf"\bthe password is{_regex}",
            rf"\bmy password is{_regex}",
            rf"\bthe password's{_regex}",
            rf"\bmy password's{_regex}",
            rf"^password{_regex}",
        ],
        padding=Pd.disabled,
    ),
    "security.password",
    "Don't put passwords in plain text.",
)

__register__ = (check,)
