"""
From whence it came.

---
layout:     post
source:     unknown
source_url: unknown
title:      whence
date:       2014-06-10 12:31:19
categories: writing
---

From whence it came.

"""

from proselint.registry.checks import Check, types

check = Check(
    check_type=types.ExistenceSimple(pattern="from whence"),
    path="misc.whence",
    message="The 'from' in 'from whence' is not needed.",
)

__register__ = (check,)
