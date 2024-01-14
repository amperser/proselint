"""Nonwords.

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

from proselint.checks import ResultCheck
from proselint.checks import preferred_forms_check


def check(text: str) -> list[ResultCheck]:
    """Suggest the preferred forms."""
    err = "nonwords.misc"
    msg = "Nonword, try '{}'."

    preferences = [
        ["doubtless' or 'undoubtedly", ["doubtlessly"]],
        ["analysis", ["analyzation"]],
        ["annoyance", ["annoyment"]],
        ["confirmand", ["confirmant"]],
        ["confirmands", ["confirmants"]],
        ["converse", ["conversate"]],
        ["cranded", ["crained"]],
        ["disbursement' or 'dispersal", ["dispersement"]],
        ["discomfort' or 'discomfiture", ["discomforture"]],
        ["effrontery", ["affrontery"]],
        ["forbearance", ["forebearance"]],
        ["improper", ["improprietous"]],
        ["inclement", ["inclimate"]],
        ["relatively low price' or 'affordability", ["relative inexpense"]],
        ["inimical", ["inimicable"]],
        ["regardless", ["irregardless"]],
        ["minimize", ["minimalize"]],
        ["minimized", ["minimalized"]],
        ["minimizes", ["minimalizes"]],
        ["minimizing", ["minimalizing"]],
        # muchly
        ["optimize", ["optimalize"]],
        ["paralysis", ["paralyzation"]],
        ["pettifog", ["pettifogger"]],
        ["proper", ["proprietous"]],
        ["quell' or 'quash", ["squelch"]],
        ["seldom", ["seldomly"]],
        # slinged
        ["thus", ["thusly"]],
        ["categorically", ["uncategorically"]],
        ["undoubtedly' or 'indubitably", ["undoubtably"]],
        ["unequivocal", ["unequivocable"]],
        ["mercilessly", ["unmercilessly"]],
        ["unrelentingly' or relentlessly", ["unrelentlessly"]],
    ]

    return preferred_forms_check(text, preferences, err, msg)
