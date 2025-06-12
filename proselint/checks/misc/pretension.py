"""Pretension.

---
layout:     post
source:     David Ogilvy
source_url: ???
title:      yelling
date:       2014-06-10 12:31:19
categories: writing
---

Never use the phrase 'all hell broke loose'.

"""
from proselint.tools import existence_check, max_errors


@max_errors(1)
def check(text):
    """Check the text."""
    err = "misc.pretension"
    msg = "Jargon words like this one are the hallmarks of a pretentious ass."

    list = [
        "reconceptualize",
        "demassification",
        "attitudinally",
        "judgmentally",
    ]

    return existence_check(text, list, err, msg)
