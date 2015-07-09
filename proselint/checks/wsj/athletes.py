# -*- coding: utf-8 -*-
"""Misspellings.

---
layout:     post
source:     The Wall Street Journal
source_url: http://amzn.to/15wF76r
title:      misspellings
date:       2014-06-10 12:31:19
categories: writing
---

Points out misspellings.

"""
from tools import memoize, preferred_forms_check


@memoize
def check(text):
    """Suggest the preferred forms."""
    err = "wsj.athletes"
    msg = "Misspelling of athlete's name. '{}' is the preferred form."

    misspellings = [
        ["Dwyane Wade",         ["Dwayne Wade"]],
        ["Miikka Kiprusoff",    ["Mikka Kiprusoff"]],
        ["Mark Buehrle",        ["Mark Buerhle"]],
        ["Skylar Diggins",      ["Skyler Diggins"]],
        ["Agnieszka Radwanska", ["Agnieska Radwanska"]],
        ["J.J. Redick",         ["J.J. Reddick"]],
        ["Manny Pacquiao",      ["Manny Packquaio"]],
        ["Antawn Jamison",      ["Antwan Jamison"]],
        ["Cal Ripken",          ["Cal Ripkin"]],
        ["Jhonny Peralta",      ["Johnny Peralta"]],
        ["Monta Ellis",         ["Monte Ellis"]],
        ["Alex Rodriguez",      ["Alex Rodriquez"]],
        ["Mark Teixeira",       ["Mark Texeira"]],
        ["Brett Favre",         ["Brett Farve"]],
        ["Torii Hunter",        ["Tori Hunter"]],
        ["Stephen Curry",       ["Stephon Curry"]],
        ["Mike Krzyzewski",     ["Mike Kryzewski"]],
    ]

    return preferred_forms_check(text, misspellings, err, msg)
