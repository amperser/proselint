"""
Names for groups of animals.

---
layout:     post
source:     Oxford Dictionaries
source_url: http://www.oxforddictionaries.com/words/what-do-you-call-a-group-of
title:      Names for groups of animals
date:       2014-06-10
categories: writing
---

Names for groups of animals.

"""

from __future__ import annotations

import re

from proselint.checks import (
    CheckResult,
    CheckSpec,
    preferred_forms_check_opti,
)

examples_pass = [
    "Smoke phrase with nothing flagged.",
    "There was a congregation of alligators.",
    "There was a wisdom of wombats.",
]

examples_fail = [
    "There was a group of alligators.",
    "There was a bunch of wombats.",
]


def _check(text: str, spec: CheckSpec) -> list[CheckResult]:
    """Check the text."""
    if not any(re.finditer("(?:group|bunch) ", text, flags=re.IGNORECASE)):
        return []

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
    items = {
        f"{generic} of {term_pair[0]}": f"{term_pair[1]} of {term_pair[0]}"
        for term_pair in term_list
        for generic in generic_terms
    }

    return preferred_forms_check_opti(text, items, spec.path, spec.msg)


check = CheckSpec(
    _check,
    "terms.venery.oxford",
    "The venery term is '{}'.",
)

__register__ = (check,)
