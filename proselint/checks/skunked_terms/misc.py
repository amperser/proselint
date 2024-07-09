"""
Skunked terms.

---
layout:     post
source:     Garner's Modern American Usage
source_url: http://bit.ly/1T4alrY
title:      Skunked terms.
date:       2014-06-10
categories: writing
---

Archaism.

"""
from __future__ import annotations

from proselint.checks import CheckResult, Pd, existence_check, registry

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "I gave an impassionate defence of the situation.",
]


def check(text: str) -> list[CheckResult]:
    """Check the text."""
    err = "skunked_terms.misc"
    msg = (
        "'{}' is a skunked term, impossible to use without issue. "
        "Find another way to say it."
    )

    skunked_terms = [
        "bona fides",
        "deceptively",
        "decimate",
        "effete",
        "fulsome",
        "hopefully",
        "impassionate",
        "Thankfully,",
    ]

    return existence_check(text, skunked_terms, err, msg, padding=Pd.sep_in_txt)


registry.register("skunked_terms.misc", check)
