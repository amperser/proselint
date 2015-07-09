# -*- coding: utf-8 -*-
"""From whence it came.

---
layout:     post
source:     unknown
source_url: unknown
title:      whence
date:       2014-06-10 12:31:19
categories: writing
---

From whence it came.

"""
from tools import existence_check, memoize


@memoize
def check(text):
    """Check the text."""
    err = "misc.whence"
    msg = u"The 'from' in 'from whence' is not needed."

    return existence_check(text, ["from whence"], err, msg)
