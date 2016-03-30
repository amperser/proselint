# -*- coding: utf-8 -*-
"""Bureaucratese.

---
layout:     post
source:     Garner's Modern American Usage
source_url: http://bit.ly/1T4alrY
title:      bureaucratese
date:       2014-06-10 12:31:19
categories: writing
---

Bureaucratese.

"""
from proselint.tools import existence_check, memoize


@memoize
def check(text):
    """Check the text."""
    err = "misc.bureaucratese"
    msg = u"'{}' is bureaucratese."

    bureaucratese = [
        "meet with your approval",
        "meets with your approval",
    ]

    return existence_check(text, bureaucratese, err, msg, join=True)
