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
    CheckResult,
    preferred_forms_check_opti,
    preferred_forms_check_regex,
    registry,
)

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "One of the greats: Cal Ripkin.",
]


def check(text: str) -> list[CheckResult]:
    """Suggest the preferred forms."""
    err = "spelling.athletes"
    msg = "Misspelling of athlete's name. '{}' is the preferred form."

    items: dict[str, str] = {
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
    }
    ret1 = preferred_forms_check_opti(text, items, err, msg)

    items_regex: dict[str, str] = {
        r"J\.J\. Reddick": "J.J. Redick",
    }
    ret2 = preferred_forms_check_regex(text, items_regex, err, msg)

    return ret1 + ret2


registry.register("spelling.athletes", check)
