"""
Lexical illusions.

---
layout:     post
source:     write-good
source_url: https://github.com/btford/write-good
title:      Lexical illusion present
date:       2014-06-10 12:31:19
categories: writing
---

A lexical illusion is when a word word is unintentionally repeated twice, and
and this happens most often between line breaks.

"""

from proselint.registry.checks import Check, types

check = Check(
    check_type=types.ExistenceSimple(
        pattern=r"\b(?<!\\|\-)(\w+(?:\s+\w+){0,3})(\s+\1)+\b",
        exceptions=(r"^had had$", r"^that that$"),
    ),
    path="lexical_illusions",
    message="There's a lexical illusion in '{}' - a phrase is repeated.",
)

__register__ = (check,)
