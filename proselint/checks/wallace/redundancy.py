# -*- coding: utf-8 -*-
"""Redundancy.

---
layout:     post
source:     David Foster Wallace
source_url: http://bit.ly/1c85lgR
title:      Redundancy
date:       2014-06-10 12:31:19
categories: writing
---

Points out use redundant phrases.

"""
from tools import memoize, preferred_forms_check


@memoize
def check(text):
    """Suggest the preferred forms."""
    err = "wallace.redundancy"
    msg = "Redundancy. Use '{}' instead of '{}'."

    redundancies = [
        ["rectangular",        ["rectangular in shape"]],
        ["audible",            ["audible to the ear"]],
    ]
    return preferred_forms_check(text, redundancies, err, msg)
