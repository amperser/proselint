# -*- coding: utf-8 -*-
"""MAU104: tortfeasor

---
layout:     post
error_code: MAU104
source:     Garner's Modern American Usage
source_url: http://amzn.to/15wF76r
title:      tortfeasor
date:       2014-06-10 12:31:19
categories: writing
---

tortfeasor (= one who commits a civil wrong) was once spelled as two words
(tort feasor), then was hyphenated, and now has been fused into a single word.


"""
from proselint.tools.supersede import supersede

check = supersede("tortfeasor", "tort feasor", "MAU104")
check = supersede("tortfeasor", "tort-feasor", "MAU104")
