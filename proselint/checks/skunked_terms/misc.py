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

from proselint.checks import CheckRegistry, CheckSpec, Existence, Pd

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "I gave an impassionate defence of the situation.",
]


check = CheckSpec(
    Existence(
        [
            "bona fides",
            "deceptively",
            "decimate",
            "effete",
            "fulsome",
            "hopefully",
            "impassionate",
            "Thankfully,",
        ],
        padding=Pd.sep_in_txt,
    ),
    "skunked_terms.misc",
    "'{}' is a skunked term, impossible to use without issue. "
    "Find another way to say it.",
)


def register_with(registry: CheckRegistry) -> None:
    """Register the check."""
    registry.register(check)
