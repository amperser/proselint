"""
Profession.

---
layout:     post
source:
source_url:
title:      Professions
date:       2014-06-10
categories: writing
---

Professions.

"""

from __future__ import annotations

from proselint.checks import CheckRegistry, CheckSpec, PreferredFormsSimple

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "I really need a shoe repair guy.",
]

check = CheckSpec(
    PreferredFormsSimple({
        "shoe repair guy": "cobbler",
        "geometrist": "geometer",
    }),
    "misc.professions",
    "'{}' is the name of that job, not '{}'.",
)


def register_with(registry: CheckRegistry) -> None:
    """Register the check."""
    registry.register(check)
