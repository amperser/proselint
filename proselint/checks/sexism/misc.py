# -*- coding: utf-8 -*-
"""Sexism.

---
layout:     post
source:     Garner's Modern American Usage
source_url: http://bit.ly/1T4alrY
title:      sexism
date:       2014-06-10 12:31:19
categories: writing
---

Points out sexist language.

"""
from proselint.tools import memoize, preferred_forms_check


@memoize
def check(text):
    """Suggest the preferred forms."""
    err = "sexism.misc"
    msg = "Gender bias. Use '{}' instead of '{}'."

    sexism = [
        ["anchor",           ["anchorman", "anchorwoman"]],
        ["chair",            ["chairman", "chairwoman"]],
        ["drafter",          ["draftman", "draftwoman"]],
        ["ombuds",           ["ombudsman", "ombudswoman"]],
        ["tribe member",     ["tribesman", "tribeswoman"]],
        ["police officer",   ["policeman", "policewoman"]],
        ["firefighter",      ["fireman", "firewoman"]],
        ["mail carrier",     ["mailman", "mailwoman"]],
        ["history",          ["herstory"]],
        ["women",            ["womyn"]],
        ["poet",             ["poetess"]],
        ["author",           ["authoress"]],
        ["waiter",           ["waitress"]],
        ["lawyer",           ["lady lawyer"]],
        ["doctor",           ["woman doctor"]],
        ["bookseller",       ["female booksalesman"]],
        ["air pilot",        ["female airman"]],
        ["executor",         ["executrix"]],
        ["prosecutor",       ["prosecutrix"]],
        ["testator",         ["testatrix"]],
        ["husband and wife", ["man and wife"]],
        ["chairs",           ["chairmen and chairs"]],
        ["men and women",    ["men and girls"]],
        ["comedian",         ["comedienne"]],
        ["confidant",        ["confidante"]],
        ["scientist",        ["woman scientist"]],
        ["scientists",       ["women scientists"]]
        # ["hero",             ["heroine"]]
    ]

    errors = preferred_forms_check(text, sexism, err, msg, ignore_case=False)

    msg = "Not a preferred form. Use '{}' instead of '{}'."
    pref = [
            ["anchor",           ["anchorperson"]],
            ["chair",            ["chairperson"]],
            ["drafter",          ["draftperson"]],
            ["ombuds",           ["ombudsperson"]],
            ["tribe member",     ["tribesperson"]],
            ["police officer",   ["policeperson"]],
            ["firefighter",      ["fireperson"]],
            ["mail carrier",     ["mailperson"]],
    ]
    for x in preferred_forms_check(text, pref, err, msg, ignore_case=False):
        errors.append(x)

    return errors
