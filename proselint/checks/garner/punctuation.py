# -*- coding: utf-8 -*-
"""MAU103: Punctuation.

---
layout:     post
error_code: MAU103
source:     Garner's Modern American Usage
source_url: http://amzn.to/15wF76r
title:      dates
date:       2014-06-10 12:31:19
categories: writing
---

Dates.

"""
from proselint.tools import existence_check, memoize


@memoize
def check_et_al(blob):
    """Check the text."""
    err = "MAU103"
    msg = u"Misplaced punctuation. It's 'et al.'"

    list = [
        "et al",
        "et. al",
        "et. al."
    ]
    return existence_check(blob, list, err, msg, join=True)
