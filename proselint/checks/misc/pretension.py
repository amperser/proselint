"""
Pretension.

---
layout:     post
source:     ???
source_url: ???
title:      pretension
date:       2014-06-10
categories: writing
---

Points out pretension.

"""

from __future__ import annotations

from proselint.checks import (
    CheckRegistry,
    CheckSpec,
    Existence,
)

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "We need to reconceptualize the project.",
]

# TODO: reimplement limit_results
check = CheckSpec(
    Existence([
        "reconceptualize",
        "demassification",
        "attitudinally",
        "judgmentally",
    ]),
    "misc.pretension.ogilvy",
    "Jargon words like this one are the hallmarks of a pretentious ass.",
)


def register_with(registry: CheckRegistry) -> None:
    """Register the check."""
    registry.register(check)
