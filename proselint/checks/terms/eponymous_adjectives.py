"""Eponymous adjectives.

---
layout:     post
source:     Garner's Modern American Usage
source_url: http://bit.ly/1T4alrY
title:      Eponymous adjectives
date:       2014-06-10 12:31:19
categories: writing
---

Eponymous adjectives.

"""
from proselint.tools import preferred_forms_check


def check(text):
    """Suggest the preferred forms."""
    err = "terms.eponymous_adjectives"
    msg = "'{}' is the preferred eponymous adjective."

    preferences = [

        ["Mephistophelean",    ["Mephistophelian"]],
        ["Shakespearean",      ["Shakespearian"]],
    ]

    return preferred_forms_check(text, preferences, err, msg)
