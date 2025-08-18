"""
Illogic.

---
layout:     post
source:     Garner's Modern American Usage
source_url: http://bit.ly/1T4alrY
title:      Illogic
date:       2014-06-10 12:31:19
categories: writing
---

Illogic.

"""

from proselint.registry.checks import Check, types

check = Check(
    check_type=types.Existence(
        items=(
            "preplan",
            "more than .{1,10} all",
            "appraisal valuations?",
            "(?:i|you|he|she|it|y'all|all y'all|you all|they) could care less",
            "least worst",
            "much-needed gaps?",
            "much-needed voids?",
            "no longer requires oxygen",
            "without scarcely",
        )
    ),
    path="misc.illogic",
    message="'{}' is illogical.",
)

check_coin_a_phrase_from = Check(
    check_type=types.ExistenceSimple(pattern="to coin a phrase from"),
    path="misc.illogic.coin",
    message="You can't coin an existing phrase. Did you mean 'borrow'?",
)

check_without_your_collusion = Check(
    check_type=types.ExistenceSimple(pattern="without your collusion"),
    path="misc.illogic.collusion",
    message="It's impossible to defraud yourself. Try 'aquiescence'.",
)

__register__ = (check, check_coin_a_phrase_from, check_without_your_collusion)
