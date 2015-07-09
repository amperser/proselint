# -*- coding: utf-8 -*-
"""Excessive apologizing.

---
layout:     post
source:     Pinker's book on writing
source_url: ???
title:      excessive apologizing
date:       2014-06-10 12:31:19
categories: writing
---

Points out excessive apologizing.

"""
from tools import memoize, existence_check


@memoize
def check(text):
    """Suggest the preferred forms."""
    err = "pinker.apologizing"
    msg = "Excessive apologizing."

    narcisissm = [
        "More research is needed",
    ]

    return existence_check(text, narcisissm, err, msg)
