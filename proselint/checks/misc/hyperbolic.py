# -*- coding: utf-8 -*-
"""EES: Hyperbolic language.

---
layout:     post
error_code: MSC
source:     ???
source_url: ???
title:      hyperbolic language
date:       2014-06-10 12:31:19
categories: writing
---

Hyperbolic language.

"""
from proselint.tools import existence_check, memoize


@memoize
def check(text):
    """Check the text."""
    err = "MSC100"
    msg = u"'{}' is hyperbolic."

    words = [
        "[a-z]*[!]{2,}",
        "[a-z]*\?{2,}"
    ]

    return existence_check(text, words, err, msg)
