"""
Debased language.

---
layout:     post
source:     ???
source_url: ???
title:      ???
date:       2014-06-10 12:31:19
categories: writing
---

Debased language.

"""

from proselint.registry.checks import Check, types

check = Check(
    check_type=types.Existence(
        items=(
            "a not unjustifiable assumption",
            "leaves much to be desired",
            "would serve no purpose",
            "a consideration which we should do well to bear in mind",
        )
    ),
    path="misc.debased",
    message="Debased language is a continuous temptation.",
)

__register__ = (check,)
