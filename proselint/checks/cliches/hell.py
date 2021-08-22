"""Too much yelling.

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
def check_repeated_exclamations(text):
    """Check the text."""
    err = "leonard.hell"
    msg = "Never use the words 'all hell broke loose'."

    regex = r"all hell broke loose"

    return existence_check(text, [regex], err, msg)
