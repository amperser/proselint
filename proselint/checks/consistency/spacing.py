# -*- coding: utf-8 -*-
"""CST200: Mixed one vs. two spaces after a period.

---
layout:     post
error_code: MAU102
source:     Consistency.
source_url: ???
title:      Mixed use of 1 vs. 2 spaces after a period.
date:       2014-06-10 12:31:19
categories: writing
---

Points out instances where there are two conventions, 1 vs. 2 spaces after
a period, in the same document.

"""
from proselint.tools import consistency_check

err = "CST200"
msg = "Inconsistent spacing after period (1 vs. 2 spaces)."

check = consistency_check([["[^\w\s] [A-Z]", "[^\w\s]  [A-Z]"]], err, msg)
