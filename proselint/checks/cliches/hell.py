"""
Too much yelling.

---
layout:     post
source:     ???
source_url: ???
title:      yelling
date:       2014-06-10
categories: writing
---

Never use the phrase 'all hell broke loose'.

"""

from __future__ import annotations

from proselint.checks import CheckRegistry, CheckSpec, Existence

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "I was at xyz and then all hell broke loose again.",
]

# TODO: limit_results
check = CheckSpec(
    Existence(["all hell broke loose"]),
    "cliches.hell",
    "Never use the words 'all hell broke loose'.",
)


def register_with(registry: CheckRegistry) -> None:
    """Register the check."""
    registry.register(check)
