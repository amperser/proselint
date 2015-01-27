# -*- coding: utf-8 -*-
"""MAU101: abbreviable

---
layout:     post
error_code: MAU101
source:     Garner's Modern American Usage
source_url: http://amzn.to/15wF76r
title:      abbreviable
date:       2014-06-10 12:31:19
categories: writing
---

It's abbreviable, not abbreviatable.

"""
import re


def check(text):

    error_code = "MAU101"
    msg = "It's abbreviable, not abbreviatable."

    errors = []
    for o in re.finditer("abbreviatable", text):
        errors.append((o.start(), o.end(), error_code, msg))

    return errors
