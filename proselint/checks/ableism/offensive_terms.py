# -*- coding: utf-8 -*-
"""Ableism.

---
layout:     post
source:     Autistic Hoya: Ableism/Language
source_url: http://www.autistichoya.com/p/ableist-words-and-terms-to-avoid.html
title:      Ableism
date:       2017-09-14
categories: writing
---

This check looks for offensive terms related to ableism issues and
raises an error marking them as offensive.

"""
from proselint.tools import memoize, existence_check


@memoize
def check(text):
    """Flag offensive words based on Autistic Hoya's Ableism/Language list."""
    err = "ableism.offensive_terms"
    msg = "Offensive term. Remove it or consider the context."

    terms_to_flag = [
        "aspie",
        "assburger",
        "barren",
        "crazy",
        "cretin",
        "crip",
        "cripple",
        "daft",
        "dumb",
        "flid",
        "fucktard",
        "freak",
        "gimp",
        "gimpy",
        "hysteria",
        "hysterical",
        "idiot",
        "idiotic",
        "imbecile",
        "insane",
        "insanity",
        "lame",
        "libtard",
        "loony",
        "lunatic",
        "maniac",
        "midget",
        "mongolism",
        "mongoloid",
        "moron",
        "psycho",
        "retard",
        "retarded",
        "tard",
        "schizo",
        "short bus",
        "simpleton",
        "spaz",
        "spazzed",
        "sperg",
        "stupid",
        "wacko",
        "whacko"
    ]

    # Test for both hyphenated and two-word forms
    terms_to_flag = [term.replace(" ","[ -]") for term in terms_to_flag]

    return existence_check(text, terms_to_flag, err, msg, join=True, ignore_case=False)
