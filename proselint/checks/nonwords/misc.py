"""
Nonwords.

---
layout:     post
source:     Garner's Modern American Usage
source_url: http://bit.ly/1T4alrY
title:      nonwords
date:       2014-06-10
categories: writing
---

Nonwords.

"""
from __future__ import annotations

from proselint.checks import CheckResult, preferred_forms_check_opti

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "The test was good irregardless.",
]


def check(text: str) -> list[CheckResult]:
    """Suggest the preferred forms."""
    err = "nonwords.misc"
    msg = "Nonword, try '{}'."

    # NOTE: or-variants have outer quotes omitted for later quoting
    items: dict[str, str] = {
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

    return preferred_forms_check_opti(text, items, err, msg)
