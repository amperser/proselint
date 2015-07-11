# -*- coding: utf-8 -*-
"""People labels.

---
layout:     post
source:     Garner's Modern American Usage
source_url: http://amzn.to/15wF76r
title:      people labels
date:       2014-06-10 12:31:19
categories: writing
---

People labels.

"""
from tools import memoize, preferred_forms_check


@memoize
def check(text):
    """Suggest the preferred forms."""
    err = "garner.people_labels"
    msg = "'{}' is the preferred people label."

    preferences = [

        ["Mephistophelean",    ["Mephistophelian"]],
        ["Shakespearean",      ["Shakespearian"]],
    ]

    return preferred_forms_check(text, preferences, err, msg)
