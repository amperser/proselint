# -*- coding: utf-8 -*-
"""PKR101: Hedging.

---
layout:     post
error_code: PKR102
source:     Pinker's book on writing
source_url: ???
title:      hedging
date:       2014-06-10 12:31:19
categories: writing
---

Points out hedging.

"""
from proselint.tools import memoize, existence_check


@memoize
def check(blob):
    """Suggest the preferred forms."""
    err = "PKR102"
    msg = "Hedging. Just say it."

    narcisissm = [
        "I would argue that",
        ", so to speak",
        "to a certain degree",
    ]

    return existence_check(blob, narcisissm, err, msg)
