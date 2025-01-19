"""
Annotation left in text.

---
layout:     post
source:     SublimeLinter-annotations
source_url: http://bit.ly/16Q7H41
title:      annotations
date:       2014-06-10
categories: writing
---

Annotation left in text.

"""

from __future__ import annotations

from proselint.checks import CheckSpec, Existence

examples_pass = [
    "Smoke phrase with nothing flagged.",
    "Add it to the to do list.",
]

examples_fail = ["Add it to the TODO list."]

check = CheckSpec(
    Existence([
        "FIXME",
        "FIX ME",
        "TODO",
        "todo",
        "ERASE THIS",
        "FIX THIS",
    ]),
    "annotations.misc",
    "Annotation left in text.",
)

__register__ = (check,)
