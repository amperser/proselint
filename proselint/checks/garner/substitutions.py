# -*- coding: utf-8 -*-
"""Brian Garner recommended substitutions from various sources.

Resources:
Garner, Modern American Usage
Garner, Modern Legal Usage
Garner, Lawprose Blog
http://www.lawprose.org/lawprose-blog/
https://abajournal.com/magazine/article/ax_these_terms_from_your_legal_writing/

---
layout:     post
source:     Various Brian Garner sources
source_url: http://www.lawprose.org/lawprose-blog/
title:      Brian Garner - Preferred Forms
date:       2018-11-19 13:35:00
categories: writing
---

"""

from proselint.tools import memoize, preferred_forms_check


@memoize
def check(text):
    """Suggest the preferred forms."""
    err = "garner.substitutions"
    msg = "Consider {}."

    # https://abajournal.com/magazine/article/ax_these_terms_from_your_legal_writing
    preferences = [
        ["'or'", [r"and(/| )or"]],
        ["'are'", ["deem"]],
        ["'if', 'except' or 'also'", ["(provided that|given that)"]],
        ["'let it be known' or 'understand'", [
            r"know all (women|men|persons) by these presents"]],
        ["'in this [agreement, section, etc]", ["herein"]],
        ["'must,' 'should,' 'is,' 'will,' or 'may'", ["shall"]],
        ["'required by''", ["pursuant to"]],
    ]

    return preferred_forms_check(text, preferences, err, msg)
