"""Misspellings.

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

from proselint.checks import ResultCheck
from proselint.checks import preferred_forms_check_opti

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "One of the greats: Cal Ripkin.",
]


def check(text: str) -> list[ResultCheck]:
    """Suggest the preferred forms."""
    err = "spelling.athletes"
    msg = "Misspelling of athlete's name. '{}' is the preferred form."

    items: dict[str, str] = {
        "Dwayne Wade": "Dwyane Wade",
        "Mikka Kiprusoff": "Miikka Kiprusoff",
        "Mark Buerhle": "Mark Buehrle",
        "Skyler Diggins": "Skylar Diggins",
        "Agnieska Radwanska": "Agnieszka Radwanska",
        "J.J. Reddick": "J.J. Redick",
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
    }

    return preferred_forms_check_opti(text, items, err, msg)
