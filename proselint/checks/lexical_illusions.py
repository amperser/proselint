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

from proselint.registry.checks import Check, Padding, engine, types

check = Check(
    check_type=types.ExistenceSimple(
        pattern=Padding.STRICT_WORDS_IN_TEXT.format(
            r"(\w+(?:\s+\w+){0,3})(\s+\1)+"
        ),
        exceptions=(r"^had had$", r"^that that$"),
    ),
    path="lexical_illusions",
    message="There's a lexical illusion in '{}' - a phrase is repeated.",
    engine=engine.Fancy(),
)

__register__ = (check,)
