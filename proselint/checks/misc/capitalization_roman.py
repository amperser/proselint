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

# TODO: this could benefit from a general roman numeral regex
# -> detect valids: ^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$
# - maybe detect with ignore-case and check for capitalization, OR
# - RE_ignorecase - RE_uppercase


def check(text: str) -> list[ResultCheck]:
    """Check the text."""
    err = "misc.capitalization.roman_num"
    msg = "Don't fail to capitalize roman numeral abbreviations."

    numerals_regex = " (I(i*)|i*)"

    items = [
        f"World War{numerals_regex}",
    ]

    return existence_check(text, items, err, msg, ignore_case=False)
