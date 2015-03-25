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
from tools import existence_check, memoize


@memoize
def check(blob):
    """Check the text."""
    err = "misc.annotations"
    msg = u"Annotation left in text."

    annotations = [
        "FIXME",
        "FIX ME",
        "TODO",
        "todo",
        "ERASE THIS",
        "FIX THIS",
    ]

    return existence_check(
        blob, annotations, err, msg, ignore_case=False, join=True)
