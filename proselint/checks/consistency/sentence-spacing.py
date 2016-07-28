# -*- coding: utf-8 -*-
"""More than one space seperating words.

---
layout:     post
source:     Consistency.
source_url: ???
title:      Using more than one space to seperate words in a sentence.
date:       2016-07-24 22:22:59
categories: writing
---

Points out instances where there are more than one space to seperate a word
from another one. It ignores extra spaces at the end of sentences if there are
no words or lines after it.

"""
from proselint.tools import consistency_check, memoize


@memoize
def check(text):
    """Check the text."""
    err = "consistency.spacing"
    msg = "More than one space after word found."

    regex = ["\s{2,}\S"]
    return consistency_check(text, [regex], err, msg)
