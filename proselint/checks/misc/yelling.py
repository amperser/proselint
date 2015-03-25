# -*- coding: utf-8 -*-
"""EES: Too much yelling.

---
layout:     post
error_code: SCH
source:     ???
source_url: ???
title:      yelling
date:       2014-06-10 12:31:19
categories: writing
---

Too much yelling.

"""
from tools import existence_check, memoize


@memoize
def check(blob):
    """Check the text."""
    err = "misc.yelling"
    msg = u"Too much yelling."

    regex = r"[^A-Z]\b((\s[A-Z]+){3,})"

    return existence_check(
        blob, [regex], err, msg, require_padding=False, ignore_case=False,
        max_errors=1, dotall=True)
