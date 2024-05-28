"""
Very.

---
layout:     post
source:     William Allen White
source_url: http://bit.ly/1XaMllw
title:      very
date:       2014-06-10
categories: writing
---

Substitute 'damn' every time you're inclined to write 'very'; your editor will
delete it and the writing will be just as it should be.

"""
from __future__ import annotations

from proselint.checks import CheckResult, existence_check, limit_results

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "The book was very interesting.",
]


@limit_results(1)
def check(text: str) -> list[CheckResult]:
    """Avoid 'very'."""
    err = "weasel_words.very"
    msg = (
        "Substitute 'damn' every time you're "
        "inclined to write 'very'; your editor will delete it "
        "and the writing will be just as it should be."
    )
    regex = "very"

    return existence_check(text, [regex], err, msg)
