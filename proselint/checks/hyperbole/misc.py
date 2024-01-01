"""Hyperbolic language.

---
layout:     post
source:     ???
source_url: ???
title:      hyperbolic language
date:       2014-06-10 12:31:19
categories: writing
---

Hyperbolic language.

"""
from __future__ import annotations

from ...lint_cache import memoize
from ...lint_checks import ResultCheck, existence_check


@memoize
def check(text: str) -> list[ResultCheck]:
    """Check the text."""
    err = "hyperbolic.misc"
    msg = "'{}' is hyperbolic."

    words = [
        r"[a-z]*[!]{2,}",
        r"[a-z]*\?{2,}",
    ]

    return existence_check(text, words, err, msg)
