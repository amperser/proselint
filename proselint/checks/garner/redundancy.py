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
import re
from proselint.tools import memoize


@memoize
def check(text):
    """Suggest the preferred forms."""
    err = "MAU103"
    msg = "'{}' is redundant, try '{}'."

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

    errors = []
    for p in redundancies:
        for r in p[1]:
            for m in re.finditer(r, text, flags=re.IGNORECASE):
                errors.append((m.start(), m.end(), err, msg.format(r, p[0])))

    return errors
