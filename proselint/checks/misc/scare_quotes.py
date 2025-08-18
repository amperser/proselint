"""
Misuse of scare quotes.

---
layout:     post
source:     Pinker's book on writing
source_url: ???
title:      misuse of scare quotes
date:       2014-06-10 12:31:19
categories: writing
---

Points out misuse of scare quotes.

"""

from proselint.registry.checks import Check, types

check = Check(
    check_type=types.ExistenceSimple(pattern=r"\bthe 'take-home message'\B"),
    path="misc.scare_quotes",
    message="Misuse of 'scare quotes'. Delete them.",
)

__register__ = (check,)
