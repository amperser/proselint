"""
Back-formations.

---
layout:     post
source:     Garner's Modern American Usage
source_url: http://bit.ly/1T4alrY
title:      back-formations
date:       2014-06-10
categories: writing
---

Back-formations.

"""

from __future__ import annotations

from proselint.checks import CheckRegistry, CheckSpec, PreferredFormsSimple

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "It is an improprietous use.",
]

check = CheckSpec(
    PreferredFormsSimple({"improprietous": "improper"}),
    "misc.back_formations",
    "Back-formation. '{}' is the preferred form.",
)


def register_with(registry: CheckRegistry) -> None:
    """Register the check."""
    registry.register(check)
