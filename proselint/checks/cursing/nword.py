"""
On 'the N word'.

---
layout:     post
source:     Louis CK
source_url: https://youtu.be/dF1NUposXVQ?t=30s
title:      the 'n-word'
date:       2014-06-10
categories: writing
---

Take responsibility with the shitty words you wanna say.

"""

from __future__ import annotations

from proselint.checks import CheckRegistry, CheckSpec, Existence

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "Have i used the n-word?",
]

check = CheckSpec(
    Existence(["the n-word"]),
    "cursing.nword",
    "Take responsibility for the shitty words you want to say.",
)


def register_with(registry: CheckRegistry) -> None:
    """Register the check."""
    registry.register(check)
