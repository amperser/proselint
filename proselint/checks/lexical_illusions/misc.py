"""Lexical illusions.

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
from proselint.tools import existence_check, memoize


@memoize
def check(text):
    """Check the text."""
    err = "lexical_illusions.misc"
    msg = u"There's a lexical illusion here: a word is repeated."

    list = [
        "the\sthe",
        "am\sam",
        "has\shas"
    ]

    return existence_check(text, list, err, msg)
