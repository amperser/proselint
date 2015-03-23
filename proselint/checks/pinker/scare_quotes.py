# -*- coding: utf-8 -*-
"""PKR101: Misuse of scare quotes.

---
layout:     post
error_code: PKR102
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
def check(blob):
    """Suggest the preferred forms."""
    err = "PKR102"
    msg = "Misuse of 'scare quotes'. Delete them."

    narcisissm = [
        "the 'take-home message'",
    ]

    return existence_check(blob, narcisissm, err, msg)
