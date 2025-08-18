"""
Jargon.

---
layout:     post
source:     Garner's Modern American Usage
source_url: http://bit.ly/1T4alrY
title:      Jargon
date:       2014-06-10
categories: writing
---



"""

from proselint.registry.checks import Check, types

check = Check(
    check_type=types.Existence(
        items=(
            "in the affirmative",
            "in the negative",
            "agendize",
            "per your order",
            "per your request",
            "disincentivize",
        )
    ),
    path="industrial_language.jargon",
    message="'{}' is jargon. Can you replace it with something more standard?",
)

__register__ = (check,)
