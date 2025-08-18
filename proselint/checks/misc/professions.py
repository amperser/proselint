"""
Profession.

---
layout:     post
source:
source_url:
title:      Professions
date:       2014-06-10 12:31:19
categories: writing
---

Professions.

"""

from proselint.registry.checks import Check, types

check = Check(
    check_type=types.PreferredFormsSimple(
        items={
            "shoe repair guy": "cobbler",
            "geometrist": "geometer",
        }
    ),
    path="misc.professions",
    message="'{}' is the name of that job.",
)

__register__ = (check,)
