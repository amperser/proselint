"""From whence it came.

---
layout:     post
source:     unknown
source_url: unknown
title:      whence
date:       2014-06-10 12:31:19
categories: writing
---

From whence it came.

"""
from __future__ import annotations

from proselint.tools import ResultCheck, existence_check, memoize


@memoize
def check(text: str) -> list[ResultCheck]:
    """Check the text."""
    err = "misc.whence"
    msg = "The 'from' in 'from whence' is not needed."

    return existence_check(text, ["from whence"], err, msg)
