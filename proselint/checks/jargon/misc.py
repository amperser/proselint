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

from __future__ import annotations

from proselint.checks import CheckRegistry, CheckSpec, Existence

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "I agree it's in the affirmative.",
]

check = CheckSpec(
    Existence([
        "in the affirmative",
        "in the negative",
        "agendize",
        "per your order",
        "per your request",
        "disincentivize",
    ]),
    "jargon.misc",
    "'{}' is jargon. Can you replace it with something more standard?",
)


def register_with(registry: CheckRegistry) -> None:
    """Register the check."""
    registry.register(check)
