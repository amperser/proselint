# -*- coding: utf-8 -*-
"""Misuse of scare quotes.

---
layout:     post
source:     Pinker's book on writing
source_url: ???
title:      misuse of scare quotes
date:       2014-06-10 12:31:19
categories: writing
---

Points out misuse of scare quotes.

"""
from tools import memoize, existence_check


@memoize
def check(text):
    """Suggest the preferred forms."""
    err = "pinker.scare_quotes"
    msg = "Misuse of 'scare quotes'. Delete them."

    narcisissm = [
        "the 'take-home message'",
    ]

    return existence_check(text, narcisissm, err, msg)
