"""Excessive apologizing.

---
layout:     post
source:     Pinker's book on writing
source_url: ???
title:      excessive apologizing
date:       2014-06-10 12:31:19
categories: writing
---

Points out excessive apologizing.

"""
from proselint.tools import existence_check, memoize


@memoize
def check(text):
    """Suggest the preferred forms."""
    err = "pinker.apologizing"
    msg = "Excessive apologizing."

    narcissism = [
        "More research is needed",
    ]

    return existence_check(text, narcissism, err, msg)
