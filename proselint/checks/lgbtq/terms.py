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

This check looks for possibly offensive terms related to LGBTQ issues and
makes more acceptable recommendations. TheNew York Times and
Associated Press have also adopted this style guide.

"""
from proselint.tools import memoize, preferred_forms_check


@memoize
def check(text):
    """Suggest preferred forms given the reference document."""
    err = "glaad.terms"
    msg = "Possibly offensive term. Consider using '{}' instead of '{}'."

    list = [
        ["gay man",            ["homosexual man"]],
        ["gay men",            ["homosexual men"]],
        ["lesbian",            ["homosexual woman"]],
        ["lesbians",           ["homosexual women"]],
        ["gay people",         ["homosexual people"]],
        ["gay couple",         ["homosexual couple"]],
        ["sexual orientation", ["sexual preference"]],
        ["openly gay",         ["admitted homosexual", "avowed homosexual"]],
        ["equal rights",       ["special rights"]]
        ]

    return preferred_forms_check(text, list, err, msg, ignore_case=False)
