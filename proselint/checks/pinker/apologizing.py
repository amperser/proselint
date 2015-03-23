# -*- coding: utf-8 -*-
"""PKR101: Excessive apologizing.

---
layout:     post
error_code: PKR102
source:     Pinker's book on writing
source_url: ???
title:      excessive apologizing
date:       2014-06-10 12:31:19
categories: writing
---

Points out excessive apologizing.

"""
from tools import memoize, existence_check


@memoize
def check(blob):
    """Suggest the preferred forms."""
    err = "PKR102"
    msg = "Excessive apologizing."

    narcisissm = [
        "More research is needed",
    ]

    return existence_check(blob, narcisissm, err, msg)
