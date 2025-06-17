"""
Professional narcissism.

---
layout:     post
source:     Pinker's book on writing
source_url: ???
title:      professional narcissism
date:       2014-06-10 12:31:19
categories: writing
---

Points out professional narcissism.

"""

from proselint.registry.checks import Check, types

check = Check(
    check_type=types.ExistenceSimple(
        pattern="In recent years, an increasing number of [a-zA-Z]{3,}sts have",
    ),
    path="misc.narcissism",
    message="Professional narcissism. Talk about the subject, not its study.",
)

__register__ = (check,)
