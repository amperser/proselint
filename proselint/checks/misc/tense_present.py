"""
Tense present.

---
layout:     post
source:     DFW's Tense Present
source_url: http://bit.ly/1c85lgR
title:      Tense present
date:       2014-06-10 12:31:19
categories: writing
---

Tense present.

"""

from proselint.registry.checks import Check, types

check = Check(
    check_type=types.Existence(
        items=(
            r"up to \d{1,3}% ?[-\x{2014}\x{2013}]{0,3} ?(?:or|and) more\W?",
            "between you and I",
            "on accident",
            "somewhat of a",
            "all it's own",
            "reason is because",
            "audible to the ear",
            "in regards to",
            "would of",
            # "and so",
            r"i ?(?:feel|am feeling|am|'m|'m feeling) nauseous",
        )
    ),
    path="misc.tense_present",
    message=r"'{}'.",
)

__register__ = (check,)
