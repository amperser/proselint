"""
Don't start a paragraph with 'But'.

---
layout:
source: Justin Jungé
source_url:
title:
date:       2016-03-10 12:31:19
categories: writing
---

Paragraphs should not start with certain bad words.

"""

from proselint.registry.checks import Check, types

check = Check(
    check_type=types.ExistenceSimple(r"(?:\n\n|^\n)But"),
    path="misc.but",
    message="No paragraph should start with a 'But'.",
    ignore_case=False,
    offset=(2, 0)
)

__register__ = (check,)
