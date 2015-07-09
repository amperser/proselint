# -*- coding: utf-8 -*-
"""Professional narcisissm.

---
layout:     post
source:     Pinker's book on writing
source_url: ???
title:      professional narcisissm
date:       2014-06-10 12:31:19
categories: writing
---

Points out academic narcisissm.

"""
from tools import memoize, existence_check


@memoize
def check(text):
    """Suggest the preferred forms."""
    err = "pinker.narcisissm"
    msg = "Professional narcisissm. Talk about the subject, not its study."

    narcisissm = [
        "In recent years, an increasing number of [a-zA-Z]{3,}sts have",
    ]

    return existence_check(text, narcisissm, err, msg)
