"""
Many a singular.

---
layout:     post
source:     Garner's Modern American Usage
source_url: http://bit.ly/1T4alrY
title:      Many a singular.
date:       2014-06-10 12:31:19
categories: writing
---

The idiom 'many a' requires a singular verb.

"""

from proselint.registry.checks import Check, types

check = Check(
    check_type=types.PreferredFormsSimple(
        items={
            "are many a": "is many a",
            "have been many a": "has been many a",
            "were many a": "was many a",
        }
    ),
    path="misc.many_a",
    message="'many a' requires a singular verb.",
)

__register__ = (check,)
