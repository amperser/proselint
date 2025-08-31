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

from proselint.registry.checks import Check, Padding, types

# Fixed pattern to prevent catastrophic backtracking
# Match repeated words or short phrases (up to 3 words)
# First check for triple repetitions, then double repetitions with exceptions
check = Check(
    check_type=types.ExistenceSimple(
        pattern=Padding.WORDS_IN_TEXT.format(
            r"(?<!-)(\w+)\s+\1(?:\s+\1)+|(?<!-)(\w+(?:\s+\w+){0,4})\s+\2"
        ),
        exceptions=(
            r"^had had$",  # Allow "had had" but not "had had had"
            r"^that that$",  # Allow "that that" but not "that that that"
            r"^can can$",  # Allow "can can" but not "can can can"
            r"^do do$",  # Allow "do do" but not "do do do"
        ),
    ),
    path="lexical_illusions",
    message="There's a lexical illusion in '{}' - a phrase is repeated.",
)

__register__ = (check,)
