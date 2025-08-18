"""
Back-formations.

---
layout:     post
source:     Garner's Modern American Usage
source_url: http://bit.ly/1T4alrY
title:      back-formations
date:       2014-06-10 12:31:19
categories: writing
---

Back-formations.

"""

from proselint.registry.checks import Check, types

check = Check(
    check_type=types.PreferredFormsSimple(items={"improprietous": "improper"}),
    path="misc.back_formations",
    message="Back-formation. '{}' is the preferred form.",
)

__register__ = (check,)
