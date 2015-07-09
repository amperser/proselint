# -*- coding: utf-8 -*-
"""Mixed one vs. two spaces after a period.

---
layout:     post
source:     Consistency.
source_url: ???
title:      Mixed use of 1 vs. 2 spaces after a period.
date:       2014-06-10 12:31:19
categories: writing
---

Points out instances where there are two conventions, 1 vs. 2 spaces after
a period, in the same document.

"""
from tools import consistency_check, memoize


@memoize
def check(text):
    """Check the text."""
    err = "consistency.spacing"
    msg = "Inconsistent spacing after period (1 vs. 2 spaces)."

    regex = ["[\.\?!] [A-Z]", "[\.\?!]  [A-Z]"]
    return consistency_check(text, [regex], err, msg)
