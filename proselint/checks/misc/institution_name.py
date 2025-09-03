"""
Common errors with institution names.

---
layout:     post
source:     Institution's webpage
source_url: http://bit.ly/2en1zbv,
title:      Institution Name
date:       2016-11-16 11:46:19
categories: writing
---

Institution names.

"""

from proselint.registry.checks import Check, types

"""
source: Virginia Tech Division of Student Affairs
source_url: http://bit.ly/2en1zbv
"""
check = Check(
    check_type=types.PreferredFormsSimple(
        items={
            "virginia polytechnic and state university": (
                "Virginia Polytechnic Institute and State University"
            ),
        }
    ),
    path="misc.institution_name",
    message="Incorrect name. Use '{}' instead of '{}'.",
)

__register__ = (check,)
