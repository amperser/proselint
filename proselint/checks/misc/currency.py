"""
Currency.

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

from proselint.checks import CheckRegistry, CheckSpec, Existence, Pd

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "It cost $10 dollars.",
]

check = CheckSpec(
    Existence(
        [r"\$[\d]* ?(?:dollars|usd|us dollars)"],
        padding=Pd.sep_in_txt,
    ),
    "misc.currency",
    "Incorrect use of symbols in {}.",
)


def register_with(registry: CheckRegistry) -> None:
    """Register the check."""
    registry.register(check)
