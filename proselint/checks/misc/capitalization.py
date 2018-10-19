# -*- coding: utf-8 -*-
"""Incorrect capitalization.

---
layout:     post
source:     Garner's Modern American Usage
source_url: http://bit.ly/1T4alrY
title:      incorrect captalization
date:       2014-06-10 12:31:19
categories: writing
---

Incorrect capitalization.

"""
from proselint.tools import (memoize,
                             preferred_forms_check,
                             split_into_sentences,
                             existence_check)


@memoize
def check(text):
    """Suggest the preferred forms."""
    err = "misc.captalization"
    msg = "Incorrect capitalization. '{}' is the preferred form."

    list = [
        ["Stone Age",          ["stone age"]],
        ["space age",          ["Space Age"]],
        ["the American West",  ["the American west"]],
        ["Mother Nature",      ["mother nature"]],
    ]

    return preferred_forms_check(text, list, err, msg, ignore_case=False)


# @memoize
# def check_seasons(text):
#     """Suggest the preferred forms."""
#     err = "MAU102"
#     msg = "Seasons shouldn't be capitalized. '{}' is the preferred form."

#     list = [
#         # ["winter",        ["Winter"]],
#         # ["fall",          ["Fall"]],
#         # ["summer",        ["Summer"]],
#         # ["spring",        ["Spring"]],
#     ]

#     return preferred_forms_check(text, list, err, msg, ignore_case=False)


@memoize
def check_months(text):
    """Suggest the preferred forms."""
    err = "MAU102"
    msg = "Months should be capitalized. '{}' is the preferred form."

    list = [

        ["January",         ["january"]],
        ["February",        ["february"]],
        # ["March",           ["march"]],
        ["April",           ["april"]],
        # ["May",             ["may"]],
        ["June",            ["june"]],
        ["July",            ["july"]],
        ["August",          ["august"]],
        ["September",       ["september"]],
        ["October",         ["october"]],
        ["November",        ["november"]],
        ["December",        ["december"]],
    ]

    return preferred_forms_check(text, list, err, msg, ignore_case=False)


@memoize
def check_days(text):
    """Suggest the preferred forms."""
    err = "MAU102"
    msg = "Days of the week should be capitalized. '{}' is the preferred form."

    list = [

        ["Monday",       ["monday"]],
        ["Tuesday",      ["tuesday"]],
        ["Wednesday",    ["wednesday"]],
        ["Thursday",     ["thursday"]],
        ["Friday",       ["friday"]],
        ["Saturday",     ["saturday"]],
        ["Sunday",       ["sunday"]],
    ]

    return preferred_forms_check(text, list, err, msg, ignore_case=False)


@memoize
def check_beginning_of_sentences(text):
    """Check for capitalizing the beginning of sentences."""
    sentences = split_into_sentences(text)
    err = "misc.capitalization"
    msg = "Sentence `{}` should begin with capital letter."
    sentences_tobe_capitalized = [_[:50] for _ in sentences if _[0].islower()]
    if len(sentences_tobe_capitalized) > 0:
        return existence_check(text,
                               sentences_tobe_capitalized,
                               err, msg, require_padding=False)
    else:
        return []