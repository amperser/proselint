"""Malaproprisms.

---
layout:     post
source:     Garner's Modern American Usage
source_url: http://bit.ly/1T4alrY
title:      Malaproprisms
date:       2014-06-10 12:31:19
categories: writing
---

Archaism.

"""
from proselint.tools import existence_check, memoize


@memoize
def check(text):
    """Check the text."""
    err = "malapropisms.misc"
    msg = "'{}' is a malapropism."

    illogics = [
        "the infinitesimal universe",
        "a serial experience",
        "attack my voracity",
    ]

    return existence_check(text, illogics, err, msg, offset=1)
