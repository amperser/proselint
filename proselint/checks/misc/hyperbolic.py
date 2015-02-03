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
from proselint.tools import blacklist, memoize

err = "MSC100"
msg = u"'{}' is hyperbolic."

words = [
    "[a-z]*[!]{2,}",
    "[a-z]*\?{2,}"
]


@memoize
def check(text):
    return blacklist(text, words, err, msg)
