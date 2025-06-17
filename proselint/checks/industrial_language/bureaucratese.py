"""
Bureaucratese.

---
layout:     post
source:     Garner's Modern American Usage
source_url: http://bit.ly/1T4alrY
title:      bureaucratese
date:       2014-06-10 12:31:19
categories: writing
---

Bureaucratese.

"""

from proselint.registry.checks import Check, types

check = Check(
    check_type=types.ExistenceSimple(pattern="meets? with your approval"),
    path="industrial_language.bureaucratese",
    message="'{}' is bureaucratese.",
)

__register__ = (check,)
