"""
Annotation left in text.

---
layout:     post
source:     SublimeLinter-annotations
source_url: http://bit.ly/16Q7H41
title:      archaism
date:       2014-06-10 12:31:19
categories: writing
---

Annotation left in text.

"""

from proselint.registry.checks import Check, types

check = Check(
    check_type=types.Existence(
        items=(
            "FIXME",
            "FIX ME",
            "TODO",
            "todo",
            "ERASE THIS",
            "FIX THIS",
        )
    ),
    path="annotations.misc",
    message="Annotation left in text.",
    ignore_case=False,
)

__register__ = (check,)
