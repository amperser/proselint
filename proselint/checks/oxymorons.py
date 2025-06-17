"""
Oxymorons.

---
layout:     post
source:     Garner's Modern American Usage
source_url: http://bit.ly/1T4alrY
title:      Oxymorons
date:       2014-06-10 12:31:19
categories: writing
---

Archaism.

"""

from proselint.registry.checks import Check, types

check = Check(
    check_type=types.Existence(
        items=(
            "amateur expert",
            "increasingly less",
            "advancing backwards?",
            "alludes explicitly to",
            "explicitly alludes to",
            "totally obsolescent",
            "completely obsolescent",
            "generally always",
            "usually always",
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
        )
    ),
    path="oxymorons",
    message="'{}' is an oxymoron.",
)

__register__ = (check,)
