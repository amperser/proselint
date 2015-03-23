# -*- coding: utf-8 -*-
"""MAU103: Sexism.

---
layout:     post
error_code: MAU103
source:     Garner's Modern American Usage
source_url: http://amzn.to/15wF76r
title:      sexism
date:       2014-06-10 12:31:19
categories: writing
---

Points out sexist language.

"""
from tools import memoize, preferred_forms_check


@memoize
def check(blob):
    """Suggest the preferred forms."""
    err = "MAU103"
    msg = "Gender bias. Use '{}' instead of '{}'."

    sexism = [
        ["anchor",           ["anchorman", "anchorwoman", "anchorperson"]],
        ["chair",            ["chairman", "chairwoman", "chairperson"]],
        ["drafter",          ["draftman", "draftwoman", "draftperson"]],
        ["ombuds",           ["ombudsman", "ombudswoman", "ombudsperson"]],
        ["tribe member",     ["tribesman", "tribeswoman", "tribesperson"]],
        ["police officer",   ["policeman", "policewoman", "policeperson"]],
        ["firefighter",      ["fireman", "firewoman", "fireperson"]],
        ["mail carrier",     ["mailman", "mailwoman", "mailperson"]],
        ["history",          ["herstory"]],
        ["women",            ["womyn"]],
        ["poet",             ["poetess"]],
        ["author",           ["authoress"]],
        ["waiter",           ["waitress"]],
        ["lawyer",           ["lady lawyer"]],
        ["doctor",           ["woman doctor"]],
        ["bookseller",       ["female booksalesman"]],
        ["air pilot",        ["femaile airman"]],
        ["executor",         ["executrix"]],
        ["prosecutor",       ["prosecutrix"]],
        ["testator",         ["testatrix"]],
        ["husband and wife", ["man and wife"]],
        ["chairs",           ["chairmen and chairs"]],
        ["men and women",    ["men and girls"]],
        ["comedian",         ["comedienne"]],
        ["confidant",        ["confidante"]],
        # ["hero",             ["heroine"]]
    ]

    return preferred_forms_check(blob, sexism, err, msg, ignore_case=False)
