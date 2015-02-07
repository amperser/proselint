# -*- coding: utf-8 -*-
"""ANN100: Annotation left in text.

---
layout:     post
error_code: ANN100
source:     SublimeLinter-annotations
source_url: http://bit.ly/16Q7H41
title:      archaism
date:       2014-06-10 12:31:19
categories: writing
---

Annotation left in text.

"""
from proselint.tools import blacklist, memoize

err = "ANN100"
msg = u"Annotation left in text."

annotations = [
    "FIXME",
    "FIX ME",
    "TODO",
    "todo",
    "ERASE THIS",
    "FIX THIS",
]


@memoize
def check(text):
    return blacklist(text, annotations, err, msg, ignore_case=False)
