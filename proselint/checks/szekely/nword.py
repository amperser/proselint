# -*- coding: utf-8 -*-
"""On 'the N word'.

---
layout:     post
source:     Louis CK
source_url: https://youtu.be/dF1NUposXVQ?t=30s
title:      the 'n-word'
date:       2014-06-10 12:31:19
categories: writing
---

Take responsibility with the shitty words you wanna say.

"""
from tools import existence_check, memoize


@memoize
def check_repeated_exclamations(text):
    """Check the text."""
    err = "skekely.nword"
    msg = u"Take responsibility for the shitty words you want to say."

    list = [
        "the n-word",
    ]

    return existence_check(text, list, err, msg)
