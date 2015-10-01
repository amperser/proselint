# -*- coding: utf-8 -*-
"""Names for groups of animals.

---
layout:     post
source:     Oxford Dictionaries
source_url: http://www.oxforddictionaries.com/words/what-do-you-call-a-group-of
title:      Names for groups of animals
date:       2014-06-10 12:31:19
categories: writing
---

Names for groups of animals.

"""
from tools import preferred_forms_check, memoize


@memoize
def check(text):
    """Check the text."""
    err = "oxford.venery_terms"
    msg = "The venery term is '{}'."

    term_list = [
        ["gorillas",     "band"],
        ["herons",       "siege"],
        ["starlings",    "murmuration"],
        ["toads",        "knot"],
        ["nightingales", "watch"],
    ]

    generic_terms = [
        "group",
        "bunch",
    ]

    list = []
    for term_pair in term_list:
        for generic in generic_terms:
            wrong = "a {} of {}".format(generic, term_pair[0])
            right = "a {} of {}".format(term_pair[1], term_pair[0])
            list += [[right, [wrong]]]

    return preferred_forms_check(text, list, err, msg)
