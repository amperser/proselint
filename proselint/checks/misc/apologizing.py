"""
Excessive apologizing.

---
layout:     post
source:     Pinker's book on writing
source_url: ???
title:      excessive apologizing
date:       2014-06-10 12:31:19
categories: writing
---

Points out excessive apologizing.

"""

from proselint.registry.checks import Check, types

check = Check(
    check_type=types.ExistenceSimple(pattern="More research is needed"),
    path="misc.apologizing",
    message="Excessive apologizing.",
)

__register__ = (check,)
