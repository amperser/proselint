"""
Very.

---
layout:     post
source:     William Allen White
source_url: http://bit.ly/1XaMllw
title:      very
date:       2014-06-10 12:31:19
categories: writing
---

Substitute 'damn' every time you're inclined to write 'very'; your editor will
delete it and the writing will be just as it should be.

"""

from proselint.registry.checks import Check, CheckFlags, types

check = Check(
    check_type=types.ExistenceSimple(pattern="very"),
    path="weasel_words.very",
    message="Substitute 'damn' every time you're "
    "inclined to write 'very'; your editor will delete it "
    "and the writing will be just as it should be.",
    flags=CheckFlags(results_limit=1),
)

__register__ = (check,)
