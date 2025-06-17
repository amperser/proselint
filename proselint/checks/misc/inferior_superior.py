"""
Inferior / Superior.

---
layout:     post
source:     Fowler's Modern English Usage
source_url: bit.ly/1YBG8QJ
title:      Inferior / Superior
date:       2016-03-10 17:27:37
categories: writing
---

Corrects 'inferior/superior than' to 'inferior/superior to'.

"""

from proselint.registry.checks import Check, types

check = Check(
    check_type=types.PreferredFormsSimple(
        items={
            "inferior than": "inferior to",
            "superior than": "superior to",
        }
    ),
    path="misc.inferior_superior",
    message="'Inferior' and 'superior' are not true comparatives. Use '{}'.",
)

__register__ = (check,)
