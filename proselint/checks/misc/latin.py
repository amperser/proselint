"""
Latin.

---
layout:     post
source:     The sense of style
source_url: http://amzn.to/1EOUZ5g
title:      ???
date:       2014-06-10 12:31:19
categories: writing
---

Latin.

"""

from proselint.registry.checks import Check, types

check = Check(
    check_type=types.PreferredFormsSimple(
        items={
            "ceteris paribus": "other things being equal",
            "inter alia": "among other things",
            "simpliciter": "in and of itself",
            "mutatis mutandis": "having made the necessary changes",
        }
    ),
    path="misc.latin",
    message="Use English. '{}' is the preferred form.",
)

__register__ = (check,)
