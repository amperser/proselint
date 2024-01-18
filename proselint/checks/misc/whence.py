"""From whence it came.

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

from proselint.checks import ResultCheck
from proselint.checks import existence_check

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
"Go back from whence you came!",
]

def check(text: str) -> list[ResultCheck]:
    """Check the text."""
    err = "misc.whence"
    msg = "The 'from' in 'from whence' is not needed."

    return existence_check(text, ["from whence"], err, msg)
