"""Oxymorons.

---
layout:     post
source:     Garner's Modern American Usage
source_url: http://bit.ly/1T4alrY
title:      Oxymorons
date:       2014-06-10
categories: writing
---

Archaism.

"""
from __future__ import annotations

from proselint.checks import ResultCheck
from proselint.checks import existence_check


def check(text: str) -> list[ResultCheck]:
    """Check the text."""
    err = "oxymorons.misc"
    msg = "'{}' is an oxymoron."

    oxymorons = [
        "amateur expert",
        "increasingly less",
        "advancing backwards?",
        "alludes explicitly to",
        "explicitly alludes to",
        "totally obsolescent",
        "completely obsolescent",
        "generally always",
        "usually always",
        "increasingly less",
        "build down",
        "conspicuous absence",
        "exact estimate",
        "found missing",
        "intense apathy",
        "mandatory choice",
        "nonworking mother",
        "organized mess",
        # "pretty ugly",
        # "sure bet",
        # "executive secretary",
    ]

    return existence_check(text, oxymorons, err, msg)
