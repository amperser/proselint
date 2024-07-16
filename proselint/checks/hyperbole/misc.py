"""
Hyperbolic language.

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

from proselint.checks import CheckRegistry, CheckSpec, Existence, Pd

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = ["So exaggerated!!!", "really??"]

check = CheckSpec(
    Existence(
        [
            r"[a-z]*[!]{2,}",
            r"[a-z]*\?{2,}",
        ],
        padding=Pd.disabled,
    ),
    "hyperbole.misc",
    "'{}' is hyperbolic.",
)


def register_with(registry: CheckRegistry) -> None:
    """Register the check."""
    registry.register(check)
