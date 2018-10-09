from proselint.tools import memoize, existence_check

"""Hedges.
---
source:     linter-just-say-no
source_url: https://github.com/lexicalunit/linter-just-say-no/blob/master/resources/hedges.cson
title:      hedges
---

"""


@memoize
def check(text):
    err = "hedges.just_say_no"
    msg = "Possible hedge word: '{}'."

    hedges = [
        "a bit",
        "a little",
        "a tad",
        "a touch",
        "at least"
        "almost",
        "apologize",
        "apparently",
        "appears",
        "approximately",
        "around",
        "basically",
        "bother",
        "could",
        "does that make sense",
        "effectively",
        "evidently",
        "fairly",
        "for the most part",
        "generally",
        "hardly",
        "hopefully",
        "I am about",
        "I think",
        "I will try",
        "I'll try",
        "I'm about",
        "I'm just trying",
        "I'm no expert",
        "I'm not an expert",
        "I'm trying",
        "in general",
        "just about",
        "just",
        "kind of",
        "largely",
        "likely",
        "mainly",
        "may",
        "maybe",
        "might",
        "more or less",
        "mostly",
        "nearly",
        "on average",
        "overall",
        "partially",
        "partly",
        "perhaps",
        "possibly",
        "potentially",
        "presumably",
        "pretty",
        "probably",
        "quite clearly",
        "quite",
        "rather",
        "really quite",
        "really",
        "relatively",
        "roughly",
        "seem",
        "seemed",
        "seems",
        "some",
        "sometimes",
        "somewhat",
        "sorry",
        "sort of",
        "suppose",
        "supposedly",
        "think",
        "typically",
        "ultimately",
        "usually",

    ]

    return existence_check(text, hedges, err, msg)
	