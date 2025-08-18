"""
Malaproprisms.

---
layout:     post
source:     Garner's Modern American Usage
source_url: http://bit.ly/1T4alrY
title:      Malaproprisms
date:       2014-06-10 12:31:19
categories: writing
---

Malapropisms.

"""

from proselint.registry.checks import Check, types

check = Check(
    check_type=types.Existence(
        items=(
            "the infinitesimal universe",
            "a serial experience",
            "attack my voracity",
        )
    ),
    path="malapropisms",
    message="'{}' is a malapropism.",
)

__register__ = (check,)
