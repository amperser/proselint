"""
Hedging.

---
layout:     post
source:     Pinker's book on writing
source_url: ???
title:      hedging
date:       2014-06-10 12:31:19
categories: writing
---

Points out hedging.

"""

from proselint.registry.checks import Check, types

check = Check(
    check_type=types.Existence(
        items=(
            "I would argue that",
            ", so to speak",
            "to a certain degree",
        )
    ),
    path="hedging",
    message="Hedging. Just say it.",
)

__register__ = (check,)
