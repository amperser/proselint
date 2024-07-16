"""
Misuse of scare quotes.

---
layout:     post
source:     Pinker's book on writing
source_url: ???
title:      misuse of scare quotes
date:       2014-06-10
categories: writing
---

Points out misuse of scare quotes.

"""

from __future__ import annotations

from proselint.checks import CheckRegistry, CheckSpec, Existence, Pd

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "What was the 'take-home message'?",
]

check = CheckSpec(
    Existence(
        [r"\bthe 'take-home message'\B"],
        padding=Pd.disabled,
    ),
    "misc.scare_quotes.pinker",
    "Misuse of 'scare quotes'. Delete them.",
)


def register_with(registry: CheckRegistry) -> None:
    """Register the check."""
    registry.register(check)
