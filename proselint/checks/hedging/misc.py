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
from proselint.tools import existence_check, memoize


@memoize
def check(text):
    """Suggest the preferred forms."""
    err = "hedging.misc"
    msg = "Hedging. Just say it."

    narcisissm = [
        "I would argue that",
        ", so to speak",
        "to a certain degree",
    ]

    return existence_check(text, narcisissm, err, msg)
