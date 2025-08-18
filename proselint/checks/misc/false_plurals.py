"""
False plurals.

---
layout:     post
source:     Garner's Modern American Usage
source_url: http://bit.ly/1T4alrY
title:      False plurals.
date:       2014-06-10 12:31:19
categories: writing
---

Using the incorrect form of the plural.

"""

from proselint.registry.checks import Check, types

check = Check(
    check_type=types.PreferredFormsSimple(
        items={
            "talismen": "talismans",
            "phenomenons": "phenomena",
        }
    ),
    path="misc.false_plurals.misc",
    message="The correct plural is '{}'.",
)

check_kudos = Check(
    check_type=types.ExistenceSimple(pattern="many kudos"),
    path="misc.false_plurals.kudos",
    message="Kudos is singular.",
)

__register__ = (check, check_kudos)
