"""Very.

---
layout:     post
source:     William Allen White
source_url: http://bit.ly/1XaMllw
title:      very
date:       2014-06-10 12:31:19
categories: writing
---

Substitute 'damn' every time you're inclined to write 'very'; your editor will
delete it and the writing will be just as it should be.

"""
from __future__ import annotations

from ...lint_checks import ResultCheck, existence_check, limit_results


@limit_results(1)
def check(text: str) -> list[ResultCheck]:
    """Avoid 'very'."""
    err = "weasel_words.very"
    msg = (
        "Substitute 'damn' every time you're "
        "inclined to write 'very'; your editor will delete it "
        "and the writing will be just as it should be."
    )
    regex = "very"

    return existence_check(text, [regex], err, msg)
