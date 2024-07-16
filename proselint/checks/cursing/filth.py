"""
Filthy words.

---
layout:     post
source:     George Carlin
source_url: https://youtu.be/kyBH5oNQOS0
title:      filthy words
date:       2014-06-10
categories: writing
---

Filthy words.

"""

from __future__ import annotations

from proselint.checks import CheckRegistry, CheckSpec, Existence

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = ["Bad shit in this phrase."]

check = CheckSpec(
    Existence([
        "shit",
        "piss",
        "fuck",
        "cunt",
        "cocksucker",
        "motherfucker",
        "tits",
        "fart",
        "turd",
        "twat",
    ]),
    "cursing.filth",
    (
        "Nobody ever tells you this as a kid, "
        "but you're supposed to avoid this word."
    ),
)


def register_with(registry: CheckRegistry) -> None:
    """Register the check."""
    registry.register(check)
