"""
Misspellings.

---
layout:     post
source:     The Wall Street Journal
source_url: http://on.wsj.com/1rksm8k
title:      misspellings of athletes
date:       2014-06-10
categories: writing
---

Points out misspellings.

"""

from __future__ import annotations

from proselint.checks import (
    CheckRegistry,
    CheckSpec,
    PreferredForms,
    PreferredFormsSimple,
)

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "One of the greats: Cal Ripkin.",
]

name = "spelling.athletes"
msg = "Misspelling of athlete's name. '{}' is the preferred form."

check = CheckSpec(
    PreferredFormsSimple({
        "Dwayne Wade": "Dwyane Wade",
        "Mikka Kiprusoff": "Miikka Kiprusoff",
        "Mark Buerhle": "Mark Buehrle",
        "Skyler Diggins": "Skylar Diggins",
        "Agnieska Radwanska": "Agnieszka Radwanska",
        "Manny Packquaio": "Manny Pacquiao",
        "Antwan Jamison": "Antawn Jamison",
        "Cal Ripkin": "Cal Ripken",
        "Johnny Peralta": "Jhonny Peralta",
        "Monte Ellis": "Monta Ellis",
        "Alex Rodriquez": "Alex Rodriguez",
        "Mark Texeira": "Mark Teixeira",
        "Brett Farve": "Brett Favre",
        "Tori Hunter": "Torii Hunter",
        "Stephon Curry": "Stephen Curry",
        "Mike Kryzewski": "Mike Krzyzewski",
    }),
    name,
    msg,
)

check_regex = CheckSpec(
    PreferredForms({
        r"J\.J\. Reddick": "J.J. Redick",
    }),
    name,
    msg,
)


def register_with(registry: CheckRegistry) -> None:
    """Register the checks."""
    registry.register_many((
        check,
        check_regex,
    ))
