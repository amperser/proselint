"""
Oxymorons.

---
layout:     post
source:     Garner's Modern American Usage
source_url: http://bit.ly/1T4alrY
title:      Oxymorons
date:       2014-06-10
categories: writing
---

Archaism.

"""

from __future__ import annotations

from proselint.checks import CheckSpec, Existence

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "He needed an exact estimate.",
    "Are we advancing backward?",
]

check = CheckSpec(
    Existence([
        "amateur expert",
        "increasingly less",
        "advancing backwards?",  # plural & singular
        "alludes explicitly to",
        "explicitly alludes to",
        "totally obsolescent",
        "completely obsolescent",
        "generally always",
        "usually always",
        "build down",
        "conspicuous absence",
        "exact estimate",
        "found missing",
        "intense apathy",
        "mandatory choice",
        "nonworking mother",
        "organized mess",
        # "pretty ugly",
        # "sure bet",
        # "executive secretary",
    ]),
    "oxymorons.misc",
    "'{}' is an oxymoron.",
)

__register__ = (check,)
