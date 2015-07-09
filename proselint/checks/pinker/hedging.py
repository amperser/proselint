# -*- coding: utf-8 -*-
"""Hedging.

---
layout:     post
source:     Pinker's book on writing
source_url: ???
title:      hedging
date:       2014-06-10 12:31:19
categories: writing
---

Points out hedging.

"""
from tools import memoize, existence_check


@memoize
def check(text):
    """Suggest the preferred forms."""
    err = "pinker.hedging"
    msg = "Hedging. Just say it."

    narcisissm = [
        "I would argue that",
        ", so to speak",
        "to a certain degree",
    ]

    return existence_check(text, narcisissm, err, msg)
