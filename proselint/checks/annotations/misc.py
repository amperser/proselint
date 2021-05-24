# -*- coding: utf-8 -*-
"""Annotation left in text.

---
layout:     post
source:     SublimeLinter-annotations
source_url: http://bit.ly/16Q7H41
title:      archaism
date:       2014-06-10 12:31:19
categories: writing
---

Annotation left in text.

"""
from proselint.tools import existence_check, memoize


@memoize
def check(text):
    """Check the text."""
    err = "annotations.misc"
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
        text, annotations, err, msg, ignore_case=False, join=True)
