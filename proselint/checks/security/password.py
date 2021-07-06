"""Password in plain text.

---
layout:     post
source:     ???
source_url: ???
title:      password in plain text
date:       2014-06-10 12:31:19
categories: writing
---

Don't put pass
"""
from proselint.tools import existence_check, memoize


@memoize
def check(text):
    """Check the text."""
    err = "security.password"
    msg = "Don't put passwords in plain text."

    pwd_regex = r"[:]? [\S]{6,30}"

    password = [
        f"the password is{pwd_regex}",
        f"my password is{pwd_regex}",
        f"the password's{pwd_regex}",
        f"my password's{pwd_regex}",
        f"^[pP]assword{pwd_regex}",
    ]

    return existence_check(text, password, err, msg)
