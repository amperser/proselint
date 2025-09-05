"""
Nonwords.

---
layout:     post
source:     Garner's Modern American Usage
source_url: http://bit.ly/1T4alrY
title:      nonwords
date:       2014-06-10 12:31:19
categories: writing
---

Nonwords.

"""

from proselint.registry.checks import Check, types

check = Check(
    check_type=types.PreferredFormsSimple(
        items={
            "affrontery": "effrontery",
            "analyzation": "analysis",
            "annoyment": "annoyance",
            "confirmant": "confirmand",
            "confirmants": "confirmands",
            "conversate": "converse",
            "crained": "cranded",
            "discomforture": "discomfort' or 'discomfiture",
            "dispersement": "disbursement' or 'dispersal",
            "doubtlessly": "doubtless' or 'undoubtedly",
            "forebearance": "forbearance",
            "improprietous": "improper",
            "inclimate": "inclement",
            "inimicable": "inimical",
            "irregardless": "regardless",
            "minimalize": "minimize",
            "minimalized": "minimized",
            "minimalizes": "minimizes",
            "minimalizing": "minimizing",
            "optimalize": "optimize",
            "paralyzation": "paralysis",
            "pettifogger": "pettifog",
            "proprietous": "proper",
            "relative inexpense": "relatively low price' or 'affordability",
            "seldomly": "seldom",
            "squelch": "quell' or 'quash",
            "thusly": "thus",
            "uncategorically": "categorically",
            "undoubtably": "undoubtedly' or 'indubitably",
            "unequivocable": "unequivocal",
            "unmercilessly": "mercilessly",
            "unrelentlessly": "unrelentingly' or relentlessly",
        }
    ),
    path="nonwords",
    message="Nonword - try '{}'.",
)

__register__ = (check,)
