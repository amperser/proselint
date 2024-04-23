"""Hyperbolic language.

---
layout:     post
source:     ???
source_url: ???
title:      hyperbolic language
date:       2014-06-10
categories: writing
---

Hyperbolic language.

"""
from __future__ import annotations

from proselint.checks import Pd
from proselint.checks import CheckResult
from proselint.checks import existence_check

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = ["So exaggerated!!!", "really??"]


def check(text: str) -> list[CheckResult]:
    """Check the text."""
    err = "hyperbole.misc"
    msg = "'{}' is hyperbolic."

    words = [
        r"[a-z]*[!]{2,}",
        r"[a-z]*\?{2,}",
    ]

    return existence_check(text, words, err, msg, padding=Pd.disabled)
