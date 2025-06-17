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
            "doubtlessly": "doubtless' or 'undoubtedly",
            "analyzation": "analysis",
            "annoyment": "annoyance",
            "confirmant": "confirmand",
            "confirmants": "confirmands",
            "conversate": "converse",
            "crained": "cranded",
            "dispersement": "disbursement' or 'dispersal",
            "discomforture": "discomfort' or 'discomfiture",
            "affrontery": "effrontery",
            "forebearance": "forbearance",
            "improprietous": "improper",
            "inclimate": "inclement",
            "relative inexpense": "relatively low price' or 'affordability",
            "inimicable": "inimical",
            "irregardless": "regardless",
            "minimalize": "minimize",
            "minimalized": "minimized",
            "minimalizes": "minimizes",
            "minimalizing": "minimizing",
            # muchly
            "optimalize": "optimize",
            "paralyzation": "paralysis",
            "pettifogger": "pettifog",
            "proprietous": "proper",
            "squelch": "quell' or 'quash",
            "seldomly": "seldom",
            # slinged
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
