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

from proselint.checks import CheckResult, existence_check, registry

examples_pass = [
    "Smoke phrase with nothing flagged.",
    "Add it to the to do list.",
]

examples_fail = ["Add it to the TODO list."]


def check(text: str) -> list[CheckResult]:
    """Check the text."""
    err = "annotations.misc"
    msg = "Annotation left in text."

    items = [
        "FIXME",
        "FIX ME",
        "TODO",
        "todo",
        "ERASE THIS",
        "FIX THIS",
    ]

    return existence_check(text, items, err, msg, ignore_case=False)


registry.register("annotations.misc", check)
