# -*- coding: utf-8 -*-
"""MAU102: academically

---
layout:     post
error_code: MAU103
source:     Garner's Modern American Usage
source_url: http://amzn.to/15wF76r
title:      academically
date:       2014-06-10 12:31:19
categories: writing
---

academically. So spelled --- not *academicly. E.g.: "The goal of the strategic
plan is to keep the university competitive economically and academicly
[read academically] through the year 2005, the release states." Frank Mastin
Jr., "84 Employees Lose Their Jobs at Tuskegee University," Montgomery
Advertiser, 2 Oct. 1997, at C2. See -IC.

LANGUAGE-CHANGE INDEX academically misspelled *academicly: Stage 1

"""
from proselint.tools.supersede import supersede

check = supersede("academically", "academicly", "MAU103")
