"""
Pretension.

---
layout:     post
source:     David Ogilvy
source_url: ???
title:      ???
date:       2014-06-10 12:31:19
categories: writing
---

Pretension.

"""

from proselint.registry.checks import Check, types

check = Check(
    check_type=types.Existence(
        items=(
            "reconceptualize",
            "demassification",
            "attitudinally",
            "judgmentally",
        )
    ),
    path="misc.pretension",
    message="Jargon words like '{}' are the hallmarks of a pretentious ass.",
)

__register__ = (check,)
