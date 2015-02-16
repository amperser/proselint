# -*- coding: utf-8 -*-
"""MAU102: Preferred forms.

---
layout:     post
error_code: MAU102
source:     Garner's Modern American Usage
source_url: http://amzn.to/15wF76r
title:      preferred forms
date:       2014-06-10 12:31:19
categories: writing
---

Points out preferred forms.

"""
from proselint.tools import memoize, preferred_forms_check


@memoize
def check(text):
    """Suggest the preferred forms."""
    err = "MAU102"
    msg = "'{}' is the preferred form."

    preferences = [

        # Obsolete words
        ["imprimatur",        ["imprimature"]],

        # Proper nouns
        ["Halloween",         ["haloween", "hallowe'en"]],
        ["Khrushchev",        ["Khruschev", "Kruschev"]],
        ["Ku Klux Klan",      ["Klu Klux Klan"]],
        ["Pontius Pilate",    ["Pontius Pilot"]],

        # Plurals
        ["sopranos",          ["soprani"]],
        ["hippopotamuses",    ["hippopotami"]],

        # Hyphenated words
        ["tortfeasor",        ["tort feasor", "tort-feasor"]],
        ["transship",         ["tranship", "trans-ship"]],
        ["transshipped",      ["transhipped", "trans-shipped"]],
        ["transshipping",     ["transhipping", "trans-shipping"]],
        ["long-standing",     ["longstanding"]],
        # ["longtime",         ["long time"]],

        # able vs. ible
        ["addable",           ["addible"]],
        ["adducible",         ["adduceable"]],
        ["impermissible",     ["impermissable"]],
        ["inadmissible",      ["inadmissable"]],
        ["inculcatable",      ["inculcatible"]],

        # er vs. or
        ["abettor",           ["abbeter"]],
        ["acquirer",          ["acquiror"]],
        ["promoter",          ["promotor"]],
        ["reckless",          ["wreckless"]],

        # in vs. un
        ["inadvisable",       ["unadvisable"]],
        ["inalienable",       ["unalienable"]],

        # Misc
        ["musical revue",     ["musical review"]],
        ["shoo-in",           ["shoe-in"]],

        # TODO, entries that are a bit complicated
        # announce
    ]

    return preferred_forms_check(text, preferences, err, msg)
