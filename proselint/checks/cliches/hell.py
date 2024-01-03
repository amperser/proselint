"""Too much yelling.

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

from ...lint_checks import ResultCheck, existence_check, limit_results


@limit_results(1)
def check_repeated_exclamations(text: str) -> list[ResultCheck]:
    """Check the text."""
    err = "leonard.hell"
    msg = "Never use the words 'all hell broke loose'."

    items = [r"all hell broke loose"]

    return existence_check(text, items, err, msg)
