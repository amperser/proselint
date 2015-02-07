# -*- coding: utf-8 -*-
"""MSC: Password in plain text.

---
layout:     post
error_code: MSC
source:     ???
source_url: ???
title:      password in plain text
date:       2014-06-10 12:31:19
categories: writing
---

Don't put pass
"""
from proselint.tools import blacklist, memoize


@memoize
def check(text):
    err = "MSC103"
    msg = u"Don't put passwords in plain text."

    pwd_regex = "[:]* [\S]{6,30}"

    password = [
        "the password is{}".format(pwd_regex),
        "my password is{}".format(pwd_regex),
        "the password's{}".format(pwd_regex),
        "my password's{}".format(pwd_regex),
    ]

    return blacklist(text, password, err, msg)
