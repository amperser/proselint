"""Pretension.

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
from proselint.tools import existence_check, max_errors, memoize


@max_errors(1)
@memoize
def check(text):
    """Check the text."""
    err = "ogilvy.pretension"
    msg = "Jargon words like this one are the hallmarks of a pretentious ass."

    list = [
        "reconceptualize",
        "demassification",
        "attitudinally",
        "judgmentally",
    ]

    return existence_check(text, list, err, msg)
