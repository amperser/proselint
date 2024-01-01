"""Pretension.

---
layout:     post
source:     ???
source_url: ???
title:      yelling
date:       2014-06-10 12:31:19
categories: writing
---

Never use the phrase 'all hell broke loose'.

"""
from __future__ import annotations

from ...lint_cache import memoize
from ...lint_checks import ResultCheck, existence_check, limit_results


@limit_results(1)
@memoize
def check(text: str) -> list[ResultCheck]:
    """Check the text."""
    err = "ogilvy.pretension"
    msg = "Jargon words like this one are the hallmarks of a pretentious ass."

    items = [
        "reconceptualize",
        "demassification",
        "attitudinally",
        "judgmentally",
    ]

    return existence_check(text, items, err, msg)
