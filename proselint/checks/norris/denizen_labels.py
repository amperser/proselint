# -*- coding: utf-8 -*-
"""Denizen labels.

---
layout:     post
source:     Mary Norris
source_url: http://nyr.kr/1rGienj
title:      denizen labels
date:       2014-06-10 12:31:19
categories: writing
---

Denizen labels.

"""
from tools import memoize, preferred_forms_check


@memoize
def check(text):
    """Suggest the preferred forms."""
    err = "norris.denizen_labels"
    msg = "Would you like '{}'?"

    preferences = [
        ["Mancunian",         ["Manchesterian"]],
        ["Mancunians",        ["Manchesterians"]],
        ["Vallisoletano",     ["Valladolidian"]],
        ["Wulfrunian",        ["Wolverhamptonian", "Wolverhamptonite"]],
        ["Novocastrian",      ["Newcastleite", "Newcastlite"]],
        ["Trifluvian",        [u"Trois-Rivièrester"]],
        ["Leodenisian",       ["Leedsian"]],
        ["Minneapolitan",     ["Minneapolisian"]],
        ["Hartlepudlian",     ["Hartlepoolian"]],
        ["Liverpudlian",      ["Liverpoolian"]],
        ["Haligonian",        ["Halifaxer"]],
        ["Varsovian",         ["Warsawer", "Warsawian"]],
        ["Providentian",      ["Providencian", "Providencer"]],
        ["Tridentine",        ["Trentian", "Trentonian"]],
    ]

    return preferred_forms_check(text, preferences, err, msg)
