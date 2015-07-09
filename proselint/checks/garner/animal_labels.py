# -*- coding: utf-8 -*-
"""Animal word.

---
layout:     post
source:     Garner's Modern American Usage
source_url: http://amzn.to/15wF76r
title:      animal words
date:       2014-06-10 12:31:19
categories: writing
---

Animal words.

"""
from tools import memoize, preferred_forms_check


@memoize
def check(text):
    """Suggest the preferred forms."""
    err = "garner.animal_labels"
    msg = "There's a word for this: '{}'."

    preferences = [

        ["accipitrine",   ["hawk-like"]],
        ["anserine",      ["goose-like"]],
        ["aquiline",      ["eagle-like"]],
        ["avine",         ["bird-like"]],
        ["cancrine",      ["crab-like"]],
        ["hircine",       ["goat-like"]],
        ["damine",        ["deer-like"]],
        ["corvine",       ["crow-like", "raven-like"]],
        ["crocodiline",   ["crocodile-like"]],
        ["crotaline",     ["rattlesnake-like"]],
        ["falconine",     ["falcon-like"]],
        ["ferine",        ["wild animal-like"]],
        ["hippopotamine", ["hippopotamus-like"]],
        ["hirundine",     ["swallow-like"]],
        ["hystricine",    ["porcupine-like"]],
        ["lacertine",     ["lizard-like"]],
        ["laridine",      ["gull-like"]],
        ["leporine",      ["hare-like"]],
        ["lumbricine",    ["earthworm-like"]],
        ["lupine",        ["wolf-like"]],
        ["murine",        ["mouse-like"]],
        ["ovine",         ["sheep-like"]],
        ["pardine",       ["leopard-like", "panther-like"]],
        ["passerine",     ["sparrow-like"]],
        ["pavonine",      ["peacock-like"]],
        ["picine",        ["woodpecker-like"]],
        ["piscine",       ["fish-like"]],
        ["ranine",        ["frog-like"]],
        ["scolopendrine", ["centipede-like"]],
        ["soricine",      ["shrew-like"]],
        ["struthionine",  ["ostrich-like"]],
        ["suilline",      ["swine-like"]],
        ["taurine",       ["bull-like", "ox-like"]],
        ["tigrine",       ["tiger-like"]],
        ["vespine",       ["wasp-like"]],
        ["viperine",      ["viper-like"]],
        ["vituline",      ["calf-like", "veal-like"]],
        ["viverrine",     ["mongoose-like"]],
        ["vulpine",       ["fox-like"]],
        ["vulturine",     ["vulture-like"]],
        ["zebrine",       ["zebra-like"]],
        ["zibeline",      ["sable-like"]],
    ]

    return preferred_forms_check(text, preferences, err, msg)
