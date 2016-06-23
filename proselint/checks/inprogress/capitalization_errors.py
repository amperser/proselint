# -*- coding: utf-8 -*-
"""Password in plain text.

---
layout:     post
source:     ???
source_url: ???
title:      Capitalization of abbreviations
date:       2014-06-10 12:31:19
categories: writing
---

In Hybrid Zones, p 255 in a citation Hughes & Huges Systems Experts and
Computers: The Systems Approach in Management and Engineering: World War Ii
and After.

World War Ii should have correct capitalization.
"""
from proselint.tools import blacklist, memoize


@memoize
def check(text):
    """Check the text."""
    err = "MSC104"
    msg = u"Don't fail to capitalize roman numeral abbreviations."

    pwd_regex = " (I(i*)|i*)"

    password = [
        "World War{}".format(pwd_regex),
    ]

    return blacklist(text, password, err, msg)
