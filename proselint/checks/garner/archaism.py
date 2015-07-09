# -*- coding: utf-8 -*-
"""Archaism.

---
layout:     post
source:     Garner's Modern American Usage
source_url: http://amzn.to/15wF76r
title:      archaism
date:       2014-06-10 12:31:19
categories: writing
---

Archaism.

"""
from tools import existence_check, memoize


@memoize
def check(text):
    """Check the text."""
    err = "garner.archaism"
    msg = u"'{}' is archaic."

    archaisms = [
        "alack",
        "anent",
        # "anon",
        "begat",
        "belike",
        "betimes",
        "boughten",
        "brocage",
        "brokage",
        "camarade",
        "chiefer",
        "chiefest",
        "Christiana",
        "completely obsolescent",
        "cozen",
        "divers",
        "deflexion",
        "durst",
        "fain",
        "forsooth",
        "foreclose from",
        "haply",
        "howbeit",
        "illumine",
        "in sooth",
        "maugre",
        "meseems",
        "methinks",
        "nigh",
        "peradventure",
        "perchance",
        "saith",
        "shew",
        "sistren",
        "spake",
        "to wit",
        "verily",
        "whilom",
        "withal",
        "wot",
        "enclosed please find",
        "please find enclosed",
        "enclosed herewith",
        "enclosed herein",
        "inforce",
        "ex postfacto",
        "foreclose from",
        "forewent",
        "for ever",
        # "designer", when used to mean a plotter against Christ
        # "demean", when used to mean "to behave" in legal contexts
        # "by the bye", # variant, modern is "by the by"
        # "comptroller" # in british english
        # "abortive" Abortive is archaic in reference to abortions of fetuses,
        # except in the sense “causing an abortion.”
    ]

    return existence_check(text, archaisms, err, msg, join=True)
