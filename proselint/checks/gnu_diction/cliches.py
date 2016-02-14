# -*- coding: utf-8 -*-
u"""Clichés.

---
layout:     post
source:     GNU diction
source_url: https://directory.fsf.org/wiki/Diction
title:      Cliches
date:       2014-06-10 12:31:19
categories: writing
---

Cliches are cliché.

"""
from tools import existence_check, memoize


@memoize
def check(text):
    """Check the text."""
    err = "gnu_diction.cliches"
    msg = u"'{}' is a cliché."

    list = [
        "a matter of concern",
        "all things being equal",
        "as a last resort",
        "attached hereto",
        "by no means",
        "conspicuous by its absence",
        "easier said than done",
        "enclosed herewith",
        "if and when",
        "in reference to",
        "in short supply",
        "in the foreseeable future",
        "in the long run",
        "in the matter of",
        "it stands to reason",
        "many and diverse",
        "on the right track",
        "par for the course",
        "please feel free to",
        "pursuant to your request",
        "regarding the matter of",
        "slowly but surely",
        "this will acknowledge",
        "we are pleased to advice",
        "we regret to inform you",
        "we wish to state",
        "you are hereby advised that",
    ]

    return existence_check(text, list, err, msg, join=True, ignore_case=True)
