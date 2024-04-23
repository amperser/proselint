"""Password in plain text.

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

from proselint.checks import Pd
from proselint.checks import CheckResult
from proselint.checks import existence_check

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "The password is 123456.",
    "My password is PASSWORD.",
]


def check(text: str) -> list[CheckResult]:
    """Check the text."""
    err = "security.password"
    msg = "Don't put passwords in plain text."

    _regex = r"[:]? [\S]{6,30}"

    items = [
        rf"\bthe password is{_regex}",
        rf"\bmy password is{_regex}",
        rf"\bthe password's{_regex}",
        rf"\bmy password's{_regex}",
        rf"^password{_regex}",
    ]

    return existence_check(text, items, err, msg, ignore_case=True, padding=Pd.disabled)
