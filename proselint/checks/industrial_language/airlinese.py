"""
Airlinese.

---
layout:     post
source:     Garner's Modern American Usage
source_url: http://bit.ly/1T4alrY
title:      Airlinese
date:       2014-06-10 12:31:19
categories: writing
---

Airlinese.

"""

from proselint.registry.checks import Check, types

check = Check(
    check_type=types.Existence(
        items=(
            "enplan(?:e|ed|ing|ement)",
            "deplan(?:e|ed|ing|ement)",
            "taking off momentarily",
        )
    ),
    path="industrial_language.airlinese",
    message="'{}' is airlinese.",
)

__register__ = (check,)
