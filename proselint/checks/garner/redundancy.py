# -*- coding: utf-8 -*-
"""MAU103: Redundancy.

---
layout:     post
error_code: MAU103
source:     Garner's Modern American Usage
source_url: http://amzn.to/15wF76r
title:      abbetor
date:       2014-06-10 12:31:19
categories: writing
---

Points out use redundant phrases.

"""
from proselint.tools import memoize, preferred_forms_check


@memoize
def check(text):
    """Suggest the preferred forms."""
    err = "MAU103"
    msg = "Redundancy. Use '{}' instead of '{}'."

    redundancies = [
        ["antithetical",      ["directly antithetical"]],
        ["ATM",               ["ATM machine"]],
        ["approximately",     ["approximately about"]],
        ["associate",         ["associate together"]],
        ["associate",         ["associate together in groups"]],
        ["vocation",          ["professional vocation"]],
        ["bivouac",           ["temporary bivouac", "bivouac camp"]],
        ["obvious",           ["blatantly obvious"]],
        ["but",               ["but nevertheless"]],
        ["charged with ...",  ["accused of a charge"]],
        ["circumstances",     ["surrounding circumstances"]],
        ["circumstances of",  ["circumstances surrounding"]],
        ["close",             ["close proximity"]],
        ["collaborator",      ["fellow collaborator"]],
        ["collaborators",     ["fellow collaborators"]],
        ["repeat",            ["repeat the same"]],
        ["repeated",          ["repeated the same"]],
        ["repeat",            ["repeat again"]],
        ["repeat",            ["repeat back"]],
        ["repay them",        ["repay them back"]],
        ["repay",             ["repay back"]],
        ["RSVP",              ["please RSVP"]],
        ["confessed",         ["self-confessed"]],
        ["software",          ["software program"]],
        ["affadavit",         ["sworn affadavit"]],
        ["blend",             ["blend together"]],
        ["connect",           ["connect together"]],
        ["consolidate",       ["consolidate together"]],
        ["couple",            ["couple together"]],
        ["merge",             ["merge together"]],
        ["while",             ["while at the same time"]],
        ["the nation",        ["the whole entire nation"]],
        ["potable water",     ["potable drinking water"]],
        ["facts",             ["true facts"]],
    ]

    return preferred_forms_check(text, redundancies, err, msg)
