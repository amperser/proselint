# -*- coding: utf-8 -*-
"""EES: Too much yelling..

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
from proselint.tools import existence_check, memoize


@memoize
def check(text):
    """Check the text."""
    err = "MAU103"
    msg = u"Too much yelling."

    regex = "[A-Z]+ [A-Z]+ [A-Z]+"
    return existence_check(text, [regex], err, msg, ignore_case=False)
