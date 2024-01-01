"""Misuse of scare quotes.

---
layout:     post
source:     Pinker's book on writing
source_url: ???
title:      misuse of scare quotes
date:       2014-06-10 12:31:19
categories: writing
---

Points out misuse of scare quotes.

"""
from __future__ import annotations

from ...lint_cache import memoize
from ...lint_checks import ResultCheck, existence_check


@memoize
def check(text: str) -> list[ResultCheck]:
    """Suggest the preferred forms."""
    err = "pinker.scare_quotes"
    msg = "Misuse of 'scare quotes'. Delete them."

    narcissism = [
        "the 'take-home message'",
    ]

    return existence_check(text, narcissism, err, msg)
