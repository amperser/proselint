"""
From whence it came.

---
layout:     post
source:     unknown
source_url: unknown
title:      whence
date:       2014-06-10
categories: writing
---

From whence it came.

"""

from __future__ import annotations

from proselint.checks import CheckSpec, Existence

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "Go back from whence you came!",
]

check = CheckSpec(
    Existence(["from whence"]),
    "misc.whence",
    "The 'from' in 'from whence' is redundant.",
)

__register__ = (check,)
