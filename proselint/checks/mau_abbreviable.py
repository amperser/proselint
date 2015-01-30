# -*- coding: utf-8 -*-
"""MAU101: Misspelling of 'abbreviable'.

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
from proselint.tools import supersede

check = supersede("abbreviable", "abbreviatable", "MAU101")
