"""Password in plain text.

---
layout:     post
source:     ???
source_url: ???
title:      Capitalization of abbreviations
date:       2014-06-10 12:31:19
categories: writing
---

In Hybrid Zones, p 255 in a citation Hughes & Huges Systems Experts and
Computers: The Systems Approach in Management and Engineering: World War Ii
and After.

World War Ii should have correct capitalization.
"""
from __future__ import annotations

from proselint.checks import ResultCheck
from proselint.checks import existence_check


def check(text: str) -> list[ResultCheck]:
    """Check the text."""
    err = "MSC104"
    msg = "Don't fail to capitalize roman numeral abbreviations."

    numerals_regex = " (I(i*)|i*)"

    items = [
        f"World War{numerals_regex}",
    ]

    return existence_check(text, items, err, msg, ignore_case=False)
