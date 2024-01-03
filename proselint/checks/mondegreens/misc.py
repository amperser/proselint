"""Mondegreens.

---
layout:     post
source:     Garner's Modern American Usage
source_url: http://bit.ly/1T4alrY
title:      mondegreens
date:       2014-06-10 12:31:19
categories: writing
---

Points out preferred form.

"""
from __future__ import annotations

from ...lint_checks import ResultCheck, preferred_forms_check


def check(text: str) -> list[ResultCheck]:
    """Suggest the preferred forms."""
    err = "misc.mondegreens"
    msg = "'{}' is the preferred form."

    items = [
        ["a girl with kaleidoscope eyes", ["a girl with colitis goes by"]],
        ["a partridge in a pear tree", ["a part-red gingerbread tree"]],
        ["attorney and notary public", ["attorney and not a republic"]],
        ["beck and call", ["beckon call"]],
        ["for all intents and purposes", ["for all intensive purposes"]],
        ["laid him on the green", ["Lady Mondegreen"]],
        ["all of the other reindeer", ["Olive, the other reindeer"]],
        ["to the manner born", ["to the manor born"]],
    ]

    return preferred_forms_check(text, items, err, msg)
