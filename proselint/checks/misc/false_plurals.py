# -*- coding: utf-8 -*-
u"""False plurals.

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
from proselint.tools import memoize, preferred_forms_check, existence_check


@memoize
def check(text):
    """Suggest the preferred forms."""
    err = "misc.false_plurals.examples"
    msg = "The plural is {}"

    preferences = [
        ["talismans", ["talismen"]],
        ["phenomena", ["phenomenons"]],
    ]

    return preferred_forms_check(text, preferences, err, msg)


@memoize
def check_kudos(text):
    """Check the text."""
    err = "misc.false_plurals.kudos"
    msg = u"Kudos is singular."

    return existence_check(text, ["many kudos"], err, msg)
