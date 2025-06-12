"""
GLAAD.

---
layout:     post
source:     GLAAD Media Reference Guide - 9th Edition
source_url: http://www.glaad.org/reference
title:      GLAAD Guidelines
date:       2016-07-06
categories: writing
---

This check looks for offensive or possibly offensive terms related to LGBTQ
issues and raises an error marking them as such or providing recommended
alternatives. The New York Times and Associated Press have also adopted this
style guide.
"""

from proselint.tools import existence_check, preferred_forms_check


def check(text):
    """Suggest preferred forms given the reference document."""
    err = "social_awareness.lgbtq.glaad"
    msg = "Possibly offensive term. Consider using '{}' instead of '{}'."

    list = [
        ["gay man", ["homosexual man"]],
        ["gay men", ["homosexual men"]],
        ["lesbian", ["homosexual woman"]],
        ["lesbians", ["homosexual women"]],
        ["gay people", ["homosexual people"]],
        ["gay couple", ["homosexual couple"]],
        ["sexual orientation", ["sexual preference"]],
        ["openly gay", ["admitted homosexual", "avowed homosexual"]],
        ["equal rights", ["special rights"]],
    ]

    return preferred_forms_check(text, list, err, msg, ignore_case=False)


def check_offensive(text):
    """Flag offensive words based on the GLAAD reference guide."""
    err = "social_awareness.lgbtq.offensive"
    msg = "Offensive term. Remove it or consider the context."
    list = [
        "fag",
        "faggot",
        "dyke",
        "sodomite",
        "homosexual agenda",
        "gay agenda",
        "transvestite",
        "homosexual lifestyle",
        "gay lifestyle",
        # homo - may create false positives without additional context
    ]

    return existence_check(text, list, err, msg, join=True, ignore_case=False)
