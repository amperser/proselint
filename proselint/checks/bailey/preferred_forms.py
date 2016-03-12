# -*- coding: utf-8 -*-
"""Preferred forms.

---
layout:     post
source:     Edward P. Bailey's "Plain English at Work"
source_url: 
title:      preferred forms
date:       2016-03-11
categories: writing
---

Points out preferred forms.

"""
from proselint.tools import memoize, preferred_forms_check

@memoize
def check(text):
    """Suggest the preferred forms."""
    err = "bailey.preferred_forms"
    msg = "'{}' is simpler."

    preferences = [
        ["about",             ["approximately"]],
        ["about/on",          ["relating to"]],
        ["agree",             ["concur"]],
        ["also",              ["furthermore", "in addition"]],
        ["ask",               ["request"]],
        ["before",            ["prior to"]],
        ["begin",             ["commence"]],
        ["buy",               ["purchase"]],
        ["can",               ["has the capability"]],
        ["carry out/do",      ["implement"]],
        ["change",            ["modify"]],
        ["check/go over",     ["review"]],
        ["check/watch",       ["monitor"]],
        ["choose",            ["elect"]],
        ["didn’t",            ["failed to"]],
        ["do",                ["accomplish"]],
        ["end",               ["conclude"]],
        ["enough",            ["sufficient"]],
        ["expect",            ["anticipate"]],
        ["few",               ["limited number"]],
        ["fill out",          ["complete"]],
        ["find",              ["locate"]],
        ["find out",          ["ascertain", "determine"]],
        ["first",             ["initial"]],
        ["follow",            ["ensue"]],
        ["go with",           ["accompany"]],
        ["happen",            ["transpire"]],
        ["have",              ["experience"]],
        ["help",              ["assist", "benefit", "cooperate", "facilitate"]],
        ["here’s",            ["attached herewith is"]],
        ["home",              ["residence"]],
        ["if",                ["in the event that", "provided that"]],
        ["instead of",        ["in lieu of"]],
        ["keep",              ["retain"]],
        ["keep/support",      ["maintain"]],
        ["later/next",        ["subsequent"]],
        ["law",               ["legislation"]],
        ["let",               ["afford an opportunity", "permit"]],
        ["let someone know",  ["notify"]],
        ["make",              ["effect"]],
        ["many/most",         ["numerous"]],
        ["must",              ["incumbent upon"]],
        ["near",              ["close proximity"]],
        ["need",              ["require"]],
        ["not enough",        ["insufficient"]],
        ["now",               ["at the present time", "presently"]],
        ["people",            ["personnel"]],
        ["place",             ["location"]],
        ["same",              ["identical"]],
        ["saw",               ["witnessed"]],
        ["see",               ["observe"]],
        ["send",              ["furnish", "transmit"]],
        ["show",              ["disclose", "exhibit", "indicate", "reveal"]],
        ["show/prove",        ["demonstrate"]],
        ["since",             ["inasmuch as", "whereas"]],
        ["soon",              ["in the near future"]],
        ["so",                ["therefore"]],
        ["start",             ["inception", "initiate"]],
        ["stop",              ["terminate"]],
        ["tell/recommend",    ["advise"]],
        ["think",             ["deem"]],
        ["time",              ["time period"]],
        ["to",                ["in an effort to"]],
        ["try",               ["endeavor"]],
        ["until",             ["until such time as"]],
        ["use",               ["utilization", "utilize"]],
        ["want",              ["desire"]],
        ["we/us",             ["this office"]],
        ["workable",          ["viable"]],
        # These appear to have too many false positives
        # ["but",                ["however"]],
        # ["say",                ["state"]],
        # ["send",               ["submit", "forward", "supply"]],
    ]

    return preferred_forms_check(text, preferences, err, msg)

