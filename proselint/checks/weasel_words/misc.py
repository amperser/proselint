"""Weasel words.

---
layout:     post
source:     write-good
source_url: https://github.com/btford/write-good
title:      Weasel words.
date:       2014-06-10 12:31:19
categories: writing
---

Weasel words clearly weaken various aspects of a number of your sentences.

"""
from proselint.lint_cache import memoize
from proselint.lint_checks import ResultCheck


@memoize
def check(text: str) -> list[ResultCheck]:

    error_code = "weasel_words.misc"
    msg = "Weasel words present."

    return []  # TODO
