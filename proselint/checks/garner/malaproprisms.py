# -*- coding: utf-8 -*-
"""MAU108: Malaproprisms.

---
layout:     post
error_code: MAU103
source:     Garner's Modern American Usage
source_url: http://amzn.to/15wF76r
title:      Malaproprisms
date:       2014-06-10 12:31:19
categories: writing
---

Archaism.

"""
from tools import existence_check, memoize


@memoize
def check(blob):
    """Check the text."""
    err = "garner.malaproprisms"
    msg = u"'{}' is a malaproprism."

    illogics = [
        "the infinitesimal universe",
        "a serial experience",
        "attack my voracity",
    ]

    return existence_check(blob, illogics, err, msg, offset=1)
