# -*- coding: utf-8 -*-
"""Inferior / Superior.

---
layout:     post
source:     Fowler's Modern English Usage
source_url: bit.ly/1YBG8QJ
title:      Inferior / Superior
date:       2016-03-10 17:27:37
categories: writing
---

Corrects 'inferior/superior than' to 'inferior/superior to'.

"""
from proselint.tools import memoize, preferred_forms_check


@memoize
def check(text):
    """Suggest the preferred forms."""
    err = "misc.inferior_superior"
    msg = "'Inferior' and 'superior' are not true comparatives. Use '{}'."

    preferences = [
        ["inferior to",         ["inferior than"]],
        ["superior to",         ["superior than"]],
    ]

    return preferred_forms_check(text, preferences, err, msg)
