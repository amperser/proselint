"""
Weasel words.

---
layout:     post
source:     write-good
source_url: https://github.com/btford/write-good
title:      Weasel words.
date:       2014-06-10
categories: writing
---

Weasel words clearly weaken various aspects of a number of your sentences.

"""

from __future__ import annotations

from proselint.checks import CheckSpec, Existence

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "Some people say this is bad.",
    "This is somewhat crazy.",
    "It is said this is wrong.",
]

check = CheckSpec(
    Existence([
        # vague
        "evidence suggests",
        "in most respects",
        "some people",
        "somewhat",
        # false authority
        "it has been decided",
        "it is said",
        "it is thought",
        "mistakes were made",
        "researchers believe",
        "some people say",
    ]),
    "weasel_words.misc",
    "Weasel words, AKA anonymous authority, present in '{}'.",
)

__register__ = (check,)
