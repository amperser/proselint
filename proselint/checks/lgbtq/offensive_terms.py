# -*- coding: utf-8 -*-
"""GLAAD.

---
layout:     post
source:     GLAAD Media Reference Guide - 9th Edition
source_url: http://www.glaad.org/reference
title:      GLAAD Guidelines
date:       2016-07-06
categories: writing
---

This check looks for offensive terms related to LGBTQ issues and
raises an error marking them as offensive. The New York Times and
Associated Press have also adopted this style guide.

"""
from proselint.tools import memoize, existence_check


@memoize
def check(text):
    """Flag offensive words based on the GLAAD reference guide."""
    err = "glaad.offensive_terms"
    msg = "Offensive term. Remove it or consider the context."

    list = [
        "fag",
        "faggot",
        "dyke",
        "sodomite",
        "homosexual agenda",
        "gay agenda",
        "transvestite",
        "homosexual lifestyle",
        "gay lifestyle"
        # homo - may create false positives without additional context
        # FIXME use topic detetor to decide whether "homo" is offensive
    ]

    return existence_check(text, list, err, msg, join=True, ignore_case=False)
