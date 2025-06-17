"""
On the 'n-word'.

---
layout:     post
source:     ???
source_url: ???
title:      the 'n-word'
date:       2014-06-10 12:31:19
categories: writing
---

Take responsibility for the words you want to say.

"""

from proselint.registry.checks import Check, types

check = Check(
    check_type=types.ExistenceSimple(pattern=r"the n-?word"),
    path="social_awareness.nword",
    message="Take responsibility for the words you want to say.",
)

__register__ = (check,)
