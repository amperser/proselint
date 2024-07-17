"""
On the 'n-word'.

---
layout:     post
source:     ???
source_url: ???
title:      the 'n-word'
date:       2014-06-10
categories: writing
---

Take responsibility for the words you want to say.

"""

from __future__ import annotations

from proselint.checks import CheckSpec, Existence

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "Have i used the n-word?",
]

check = CheckSpec(
    Existence(["the n-word", "the n word"]),
    "cursing.nword",
    "Take responsibility for the words you want to say.",
)

__register__ = (check,)
