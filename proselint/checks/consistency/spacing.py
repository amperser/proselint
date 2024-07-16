"""
Mixed one vs. two spaces after a period.

---
layout:     post
source:     Consistency.
source_url: ???
title:      Mixed use of 1 vs. 2 spaces after a period.
date:       2014-06-10
categories: writing
---

Points out instances where there are two conventions, 1 vs. 2 spaces after
a period, in the same document.

"""

from __future__ import annotations

from proselint.checks import CheckRegistry, CheckSpec, Consistency

examples_pass = [
    "Smoke phrase with nothing flagged.",
    "This is good. Only one space each time. Every time.",
]

examples_fail = ["This is bad.  Not consistent. At all."]

check = CheckSpec(
    Consistency([(r"[\.\?!] [A-Z]", r"[\.\?!]  [A-Z]")]),
    "consistency.spacing",
    "Inconsistent spacing after period (1 vs. 2 spaces).",
    ignore_case=False,
)


def register_with(registry: CheckRegistry) -> None:
    """Register the check."""
    registry.register(check)
