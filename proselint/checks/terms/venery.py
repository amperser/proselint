"""Names for groups of animals.

---
layout:     post
source:     Oxford Dictionaries
source_url: http://www.oxforddictionaries.com/words/what-do-you-call-a-group-of
title:      Names for groups of animals
date:       2014-06-10 12:31:19
categories: writing
---

Names for groups of animals.

"""
from __future__ import annotations

import re

from proselint.checks import ResultCheck
from proselint.checks import preferred_forms_check


def check(text: str) -> list[ResultCheck]:
    """Check the text."""
    if not any(re.finditer("group|bunch", text, flags=re.IGNORECASE)):
        return []

    err = "oxford.venery_terms"
    msg = "The venery term is '{}'."

    term_list = [
        ["alligators", "congregation"],
        ["antelopes", "herd"],
        ["baboons", "troop"],
        ["badgers", "cete"],
        ["bats", "colony"],
        ["bears", "sloth"],
        ["buffalo", "herd"],
        ["bullfinches", "bellowing"],
        ["caribou", "herd"],
        ["cats", "glaring"],
        ["caterpillars", "army"],
        ["cockroaches", "intrusion"],
        ["coyotes", "pack"],
        ["crows", "murder"],
        ["dogs", "pack"],
        ["eagles", "convocation"],
        ["emus", "mob"],
        ["flamingos", "stand"],
        ["frogs", "army"],
        ["goldfinches", "charm"],
        ["gorillas", "band"],
        ["guineafowl", "rasp"],
        ["hedgehogs", "array"],
        ["herons", "siege"],
        ["hogs", "parcel"],
        ["hyenas", "cackle"],
        ["ibex", "herd"],
        ["iguanas", "mess"],
        ["lions", "pride"],
        ["locusts", "plague"],
        ["mackerel", "shoal"],
        ["mares", "stud"],
        ["minnows", "shoal"],
        ["moose", "herd"],
        ["mosquitoes", "scourge"],
        ["nightingales", "watch"],
        ["oysters", "bed"],
        ["partridges", "covey"],
        ["pelicans", "pod"],
        ["raccoons", "gaze"],
        ["ravens", "unkindness"],
        ["rhinoceroses", "crash"],
        ["sea urchins", "sea"],
        ["starlings", "murmuration"],
        ["toads", "knot"],
        ["wombats", "wisdom"],
        ["woodcocks", "fall"],
        ["woodpeckers", "descent"],
        ["wrens", "herd"],
    ]

    generic_terms = [
        "group",
        "bunch",
    ]

    # NOTE: python automatically caches this calculation for reruns
    #       check with benchmark_checks.py

    items = []
    for term_pair in term_list:
        for generic in generic_terms:
            wrong = f"a {generic} of {term_pair[0]}"
            right = f"a {term_pair[1]} of {term_pair[0]}"
            items += [[right, [wrong]]]

    return preferred_forms_check(text, items, err, msg)
