"""
Too much yelling.

---
layout:     post
source:     ???
source_url: ???
title:      yelling
date:       2014-06-10 12:31:19
categories: writing
---

Never use the phrase 'all hell broke loose'.

"""

from proselint.registry.checks import Check, types

check = Check(
    check_type=types.ExistenceSimple(pattern="all hell broke loose"),
    path="cliches.hell",
    message="Never use the phrase 'all hell broke loose'.",
)

__register__ = (check,)
