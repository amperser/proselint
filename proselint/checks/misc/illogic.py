"""
Illogic.

---
layout:     post
source:     Garner's Modern American Usage
source_url: http://bit.ly/1T4alrY
title:      Illogic
date:       2014-06-10
categories: writing
---

Archaism.

"""

from __future__ import annotations

from proselint.checks import CheckRegistry, CheckSpec, Existence

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "We should preplan the trip.",
    "To coin a phrase from him, No diggity",
    "Not Without your collusion you won't'.",
    "it fills a much-needed gap",
]

check = CheckSpec(
    Existence([
        "preplan",
        "more than .{1,10} all",
        "appraisal valuations?",  # singular & plural
        "(?:i|you|he|she|it|y'all|all y'all|you all|they) could care less",
        "least worst",
        "much-needed gaps?",  # singular & plural
        "much-needed voids?",  # singular & plural
        "no longer requires oxygen",
        "without scarcely",
    ]),
    "misc.illogic",
    "'{}' is illogical.",
)

check_coin_a_phrase_from = CheckSpec(
    Existence(["to coin a phrase from"]),
    "misc.illogic.coin",
    "You can't coin an existing phrase. Did you mean 'borrow'?",
)

check_without_your_collusion = CheckSpec(
    Existence(["without your collusion"]),
    "misc.illogic.collusion",
    "It's impossible to defraud yourself. Try 'aquiescence'.",
)


def register_with(registry: CheckRegistry) -> None:
    """Register the checks."""
    registry.register_many((
        check,
        check_coin_a_phrase_from,
        check_without_your_collusion,
    ))
