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

from proselint.checks import (
    CheckRegistry,
    CheckSpec,
    Existence,
)

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "The book was very interesting.",
]


# TODO: reimplement limit_results
check = CheckSpec(
    Existence(["very"]),
    "weasel_words.very",
    "Substitute 'damn' every time you're "
    "inclined to write 'very'; your editor will delete it "
    "and the writing will be just as it should be.",
)


def register_with(registry: CheckRegistry) -> None:
    """Register the check."""
    registry.register(check)
