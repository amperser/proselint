"""
Inconsistent spelling.

---
layout:     post
source:     Intelligent Editing Ltd.
source_url: http://bit.ly/1x3hYj7
title:      Inconsistent spelling
date:       2014-06-10
categories: writing
---

Intelligent Editing Ltd. says:

> Some words have more than one correct spelling. American, British, Australian
and Canadian English all have their own preferences. Even within those, there
can be multiple spellings. For example, in the UK 'realise' is often preferred.
However, 'realize' has been used in British-English for centuries and is
preferred in the Oxford English Dictionary. However, no matter which spelling
is preferred, one thing is always wrong: you mustn't use two different
spellings in the same document.
"""
from __future__ import annotations

from proselint.checks import CheckResult, consistency_check, registry

examples_pass = [
    "Smoke phrase with nothing flagged.",
    "The centre for the arts is the art centre.",
    "The center for the arts is the art center.",
]

examples_fail = [
    "The centre of the arts is the art center.",
]


def check(text: str) -> list[CheckResult]:
    """Check the text."""
    err = "consistency.spelling"
    msg = "Inconsistent spelling of '{}' (vs. '{}')."

    word_pairs = [
        ["advisor", "adviser"],
        # ["analyse", "analyze"],
        ["centre", "center"],
        ["colour", "color"],
        ["emphasise", "emphasize"],
        ["finalise", "finalize"],
        ["focussed", "focused"],
        ["labour", "labor"],
        ["learnt", "learned"],
        ["organise", "organize"],
        ["organised", "organized"],
        ["organising", "organizing"],
        ["recognise", "recognize"],
    ]
    # TODO: add more BE, UE, even generalize [a-z]+(ize|ized|izing)?

    return consistency_check(text, word_pairs, err, msg, ignore_case=True)


registry.register("consistency.spelling", check)
