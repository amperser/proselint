# -*- coding: utf-8 -*-
"""Profession.

---
layout:     post
source:
source_url:
title:      Professions
date:       2014-06-10 12:31:19
categories: writing
---

Professions.

"""
from proselint.tools import memoize, preferred_forms_check


@memoize
def check(text):
    """Suggest the preferred forms."""
    err = "misc.professions"
    msg = "'{}' is the name of that job."

    preferences = [

        ["cobbler",    ["shoe repair guy"]],
        ["geometer",   ["geometrist"]],
    ]

    return preferred_forms_check(text, preferences, err, msg)
