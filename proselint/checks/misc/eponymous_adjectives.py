# -*- coding: utf-8 -*-
"""Eponymous adjectives.

---
layout:     post
source:     Garner's Modern American Usage
source_url: http://amzn.to/15wF76r
title:      Eponymous adjectives
date:       2014-06-10 12:31:19
categories: writing
---

Eponymous adjectives.

"""
from tools import memoize, preferred_forms_check


@memoize
def check(text):
    """Suggest the preferred forms."""
    err = "garner.eponymous_adjective"
    msg = "'{}' is the preferred eponymous adjective."

    preferences = [

        ["Mephistophelean",    ["Mephistophelian"]],
        ["Shakespearean",      ["Shakespearian"]],
    ]

    return preferred_forms_check(text, preferences, err, msg)
