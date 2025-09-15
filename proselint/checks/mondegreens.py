"""
Mondegreens.

---
layout:     post
source:     Garner's Modern American Usage
source_url: http://bit.ly/1T4alrY
title:      mondegreens
date:       2014-06-10 12:31:19
categories: writing
---

Mondegreens.

"""

from proselint.registry.checks import Check, types

check = Check(
    check_type=types.PreferredFormsSimple(
        items={
            "a girl with colitis goes by": "a girl with kaleidoscope eyes",
            "a part-red gingerbread tree": "a partridge in a pear tree",
            "attorney and not a republic": "attorney and notary public",
            "beckon call": "beck and call",
            "for all intensive purposes": "for all intents and purposes",
            "lady mondegreen": "laid him on the green",
            "olive, the other reindeer": "all of the other reindeer",
            "to the manor born": "to the manner born",
        }
    ),
    path="mondegreens",
    message="'{}' is the preferred form.",
)

__register__ = (check,)
