# -*- coding: utf-8 -*-
"""Hyperbolic language.

---
layout:     post
source:     ???
source_url: ???
title:      hyperbolic language
date:       2014-06-10 12:31:19
categories: writing
---

Hyperbolic language.

"""
from tools import existence_check, memoize


@memoize
def check(text):
    """Check the text."""
    err = "misc.hyperbolic"
    msg = u"'{}' is hyperbolic."

    words = [
        "[a-z]*[!]{2,}",
        "[a-z]*\?{2,}"
    ]

    return existence_check(text, words, err, msg)
