"""WGD200: Lexical illusions.

---
layout:     post
error_code: WGD200
source:     write-good
source_url: https://github.com/btford/write-good
title:      Lexical illusion present
date:       2014-06-10 12:31:19
categories: writing
---

A lexical illusion happens when a word word is unintentiall repeated twice, and
and this happens most often between line breaks.

"""
from proselint.tools import existence_check, memoize


@memoize
def check(text):
    """Check the text."""
    err = "WGD105"
    msg = u"There's a lexical illusion here: a word is repeated."

    commercialese = [
        "the\sthe",
        "is\sis"
    ]

    return existence_check(text, commercialese, err, msg)
