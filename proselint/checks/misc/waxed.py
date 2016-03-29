"""Waxed lyrical.

---
layout:     post
source:     Fowler's Modern English Usage
source_url: bit.ly/1YBG8QJ
title:      Waxed lyrical
date:       2016-03-10 14:48:42
categories: writing
---

Fowler's says:
Its primary meaning 'grow larger, increase' (as opposed to 'wane') leads
naturally to the sense 'pass into a specified state or mood, begin to use a
specified tone. In this meaning a following modifier must be an adj. not an
adverb ('He waxed enthusiastic [not enthusiastically] about Australia').
"""
from proselint.tools import memoize, preferred_forms_check


@memoize
def check(text):
    """Suggest the preferred forms."""
    err = "misc.waxed"
    msg = u"The modifier following 'waxed' must be an adj.: '{}' is correct"

    waxes = ["wax", "waxes", "waxed", "waxing"]
    modifiers = [("ebullient", "ebulliently"),
                 ("ecstatic", "ecstatically"),
                 ("eloquent", "eloquently"),
                 ("enthusiastic", "enthusiastically"),
                 ("euphoric", "euphorically"),
                 ("indignant", "indignantly"),
                 ("lyrical", "lyrically"),
                 ("melancholic", "melancholically"),
                 ("metaphorical", "metaphorically"),
                 ("nostalgic", "nostalgically"),
                 ("patriotic", "patriotically"),
                 ("philosophical", "philosophically"),
                 ("poetic", "poetically"),
                 ("rhapsodic", "rhapsodically"),
                 ("romantic", "romantically"),
                 ("sentimental", "sentimentally")
                 ]

    def pairs(word):
        return [[word + ' ' + pair[0], [word + ' ' + pair[1]]]
                for pair in modifiers]

    preferred = []
    for word in waxes:
        preferred += pairs(word)

    return preferred_forms_check(text, preferred, err, msg)
