"""
On the 'n-word'.

---
layout:     post
source:     ???
source_url: ???
title:      the 'n-word'
date:       2014-06-10 12:31:19
categories: writing
---

Take responsibility for the words you want to say.

"""

from proselint.tools import existence_check


def check(text):
    """Check the text."""
    err = "social_awareness.nword"
    msg = "Take responsibility for the words you want to say."

    list = [
        "the n-word",
        "the n word",
    ]

    return existence_check(text, list, err, msg)
