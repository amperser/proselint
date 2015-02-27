# -*- coding: utf-8 -*-
"""MAU109: Denizen labels.

---
layout:     post
error_code: MAU109
source:     Garner's Modern American Usage
source_url: http://amzn.to/15wF76r
title:      denizen labels
date:       2014-06-10 12:31:19
categories: writing
---

Denizen labels.

"""
from proselint.tools import memoize, preferred_forms_check


@memoize
def check(text):
    """Suggest the preferred forms."""
    err = "MAU109"
    msg = "'{}' is the preferred denizen label."

    preferences = [

        ["Michigander",       ["Michiganite"]],
        ["Indianan",          ["Indianian"]],
        ["Illinoisan",        ["Illinoisian"]],
        ["Saudi",             ["Saudi Arabian"]],
    ]

    return preferred_forms_check(text, preferences, err, msg)
