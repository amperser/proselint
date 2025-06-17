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

from proselint.registry.checks import Check, types

check_terms = Check(
    check_type=types.PreferredFormsSimple(
        items={
            "homosexual man": "gay man",
            "homosexual men": "gay men",
            "homosexual woman": "lesbian",
            "homosexual women": "lesbians",
            "homosexual people": "gay people",
            "homosexual couple": "gay couple",
            "sexual preference": "sexual orientation",
            "admitted homosexual": "openly gay",
            "avowed homosexual": "openly gay",
            "special rights": "equal rights",
        }
    ),
    path="social_awareness.lgbtq.terms",
    message="Possibly offensive term. Consider using '{}' instead of '{}'.",
)

check_offensive = Check(
    check_type=types.Existence(
        items=(
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
        )
    ),
    path="social_awareness.lgbtq.offensive",
    message="Offensive term. Remove it or consider the context.",
)

__register__ = (check_terms, check_offensive)
