# -*- coding: utf-8 -*-
"""Password in plain text.

---
layout:     post
source:     ???
source_url: ???
title:      password in plain text
date:       2014-06-10 12:31:19
categories: writing
---

Don't put pass
"""
from tools import existence_check, memoize


@memoize
def check(text):
    """Check the text."""
    err = "misc.password"
    msg = u"Don't put passwords in plain text."

    pwd_regex = "[:]? [\S]{6,30}"

    password = [
        "the password is{}".format(pwd_regex),
        "my password is{}".format(pwd_regex),
        "the password's{}".format(pwd_regex),
        "my password's{}".format(pwd_regex),
        "^[pP]assword{}".format(pwd_regex),
    ]

    return existence_check(text, password, err, msg)
