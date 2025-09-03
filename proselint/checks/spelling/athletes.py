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
            "dwayne wade": "Dwyane Wade",
            "mikka kiprusoff": "Miikka Kiprusoff",
            "mark buerhle": "Mark Buehrle",
            "skyler diggins": "Skylar Diggins",
            "agnieska radwanska": "Agnieszka Radwanska",
            r"j\.j\. reddick": r"J\.J\. Redick",
            "manny packquaio": "Manny Pacquiao",
            "antwan jamison": "Antawn Jamison",
            "cal ripkin": "Cal Ripken",
            "johnny peralta": "Jhonny Peralta",
            "monte ellis": "Monta Ellis",
            "alex rodriquez": "Alex Rodriguez",
            "mark texeira": "Mark Teixeira",
            "brett farve": "Brett Favre",
            "tori hunter": "Torii Hunter",
            "stephon curry": "Stephen Curry",
            "mike kryzewski": "Mike Krzyzewski",
        }
    ),
    path="spelling.athletes",
    message="Misspelling of athlete's name. '{}' is the preferred form.",
)

__register__ = (check,)
