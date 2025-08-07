"""
Skunked terms.

---
layout:     post
source:     Garner's Modern American Usage
source_url: http://bit.ly/1T4alrY
title:      Skunked terms.
date:       2014-06-10 12:31:19
categories: writing
---

Skunked terms.

"""

from proselint.registry.checks import Check, types

check = Check(
    check_type=types.Existence(
        items=(
            "bona fides",
            "deceptively",
            "decimate",
            "effete",
            "fulsome",
            "hopefully",
            "impassionate",
            "Thankfully,",
        )
    ),
    path="skunked_terms",
    message=(
        "'{}' is a a skunked term - impossible to use without issue."
        " Find some other way to say it."
    ),
)

__register__ = (check,)
