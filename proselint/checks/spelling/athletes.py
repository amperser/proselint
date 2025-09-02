"""
Misspellings.

---
layout:     post
source:     The Wall Street Journal
source_url: http://on.wsj.com/1rksm8k
title:      misspellings
date:       2014-06-10 12:31:19
categories: writing
---

Points out misspellings.

"""

from proselint.registry.checks import Check, types

check = Check(
    check_type=types.PreferredFormsSimple(
        items={
            "Dwayne Wade": "Dwyane Wade",
            "Mikka Kiprusoff": "Miikka Kiprusoff",
            "Mark Buerhle": "Mark Buehrle",
            "Skyler Diggins": "Skylar Diggins",
            "Agnieska Radwanska": "Agnieszka Radwanska",
            r"J\.J\. Reddick": r"J\.J\. Redick",
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
    ),
    path="spelling.athletes",
    message="Misspelling of athlete's name. '{}' is the preferred form.",
    ignore_case=False,
)

__register__ = (check,)
