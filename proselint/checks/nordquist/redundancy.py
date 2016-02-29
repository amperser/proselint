# -*- coding: utf-8 -*-
"""Redundancy.

---
layout:     post
source:     Richard Nordquist
source_url: http://grammar.about.com/bio/Richard-Nordquist-22176.htm
title:      abbetor
date:       2014-06-10 12:31:19
categories: writing
---

Points out use redundant phrases.

"""
from tools import memoize, preferred_forms_check


@memoize
def check(text):
    """Suggest the preferred forms."""
    err = "nordquist.redundancy"
    msg = "Redundancy. Use '{}' instead of '{}'."

    redundancies = [
        ["essential",          ["absolutely essential"]],
        ["necessary",          ["absolutely necessary"]],
        ["a.m.",               ["a.m. in the morning"]],
        ["p.m.",               ["p.m. at night"]],
    ]
    return preferred_forms_check(text, redundancies, err, msg)
