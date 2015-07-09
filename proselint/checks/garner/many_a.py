# -*- coding: utf-8 -*-
u"""Many a singular.

---
layout:     post
source:     Garner's Modern American Usage
source_url: http://amzn.to/15wF76r
title:      Many a singular.
date:       2014-06-10 12:31:19
categories: writing
---

The idiom 'many a' requires a singular verb.

"""
from tools import memoize, preferred_forms_check


@memoize
def check(text):
    """Suggest the preferred forms."""
    err = "ganer.many_a"
    msg = "'many a' requires a singular verb."

    preferences = [
        ["is many a",          ["are many a"]],
        ["has been many a",    ["have been many a"]],
        ["was many a",         ["were many a"]],
    ]

    return preferred_forms_check(text, preferences, err, msg)
