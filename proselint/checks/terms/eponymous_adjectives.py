"""
Eponymous adjectives.

---
layout:     post
source:     Garner's Modern American Usage
source_url: http://bit.ly/1T4alrY
title:      Eponymous adjectives
date:       2014-06-10 12:31:19
categories: writing
---

Eponymous adjectives.

"""

from proselint.registry.checks import Check, types

check = Check(
    check_type=types.PreferredFormsSimple(
        items={
            "mephistophelian": "Mephistophelean",
            "shakespearian": "Shakespearean",
        }
    ),
    path="terms.eponymous_adjectives",
    message="'{}' is the preferred eponymous adjective.",
)

__register__ = (check,)
