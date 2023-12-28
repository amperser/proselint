"""First line is always wrong.

---
layout:     post
source:     Nobody
source_url: ???
title:      First line is always wrong.
date:       2014-06-10 12:31:19
categories: writing
---

The first line always is always wrong.

"""
from __future__ import annotations

from proselint.tools import ResultCheck, reverse


def check(text: str) -> list[ResultCheck]:
    """Check the text."""
    error_code = "example.first"
    msg = "First line always has an error."

    reverse(text)

    return [(1, 1, error_code, msg, None)]
