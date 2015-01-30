# -*- coding: utf-8 -*-
"""MAU105: Misspelling of 'addable'.

---
layout:     post
error_code: MAU105
source:     Garner's Modern American Usage
source_url: http://amzn.to/15wF76r
title:      acquirer
date:       2014-06-10 12:31:19
categories: writing
---

addable. So spelled---not *addible. See - ABLE (A).

"""
from proselint.tools import supersede

check = supersede("addable", "addible", "MAU105")
