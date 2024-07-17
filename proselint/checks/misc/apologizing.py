"""
Excessive apologizing.

---
layout:     post
source:     Pinker's book on writing
source_url: ???
title:      excessive apologizing
date:       2014-06-10
categories: writing
---

Points out excessive apologizing.

"""

from __future__ import annotations

from proselint.checks import CheckSpec, Existence

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "To say something more research is needed.",
]

check = CheckSpec(
    Existence(["more research is needed"]),
    "misc.apologizing.pinker",
    "Excessive apologizing.",
)

__register__ = (check,)
