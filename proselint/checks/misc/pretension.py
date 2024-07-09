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
    CheckResult,
    existence_check,
    limit_results,
    registry,
)

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "We need to reconceptualize the project.",
]


@limit_results(1)
def check(text: str) -> list[CheckResult]:
    """Check the text."""
    err = "misc.pretension.ogilvy"
    msg = "Jargon words like this one are the hallmarks of a pretentious ass."

    items = [
        "reconceptualize",
        "demassification",
        "attitudinally",
        "judgmentally",
    ]

    return existence_check(text, items, err, msg)


registry.register("misc.pretension.ogilvy", check)
