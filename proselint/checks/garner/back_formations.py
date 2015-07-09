# -*- coding: utf-8 -*-
"""Back-formations.

---
layout:     post
source:     Garner's Modern American Usage
source_url: http://amzn.to/15wF76r
title:      back-formations
date:       2014-06-10 12:31:19
categories: writing
---

Back-formations.

"""
from tools import memoize, preferred_forms_check


@memoize
def check(text):
    """Suggest the preferred forms."""
    err = "garner.back_formations"
    msg = "Back-formation. '{}' is the preferred form."

    list = [
        ["improper",       ["improprietous"]],
    ]

    return preferred_forms_check(text, list, err, msg)
