"""
Punctuation.

---
layout:     post
source:     Garner's Modern American Usage
source_url: http://bit.ly/1T4alrY
title:      dates
date:       2014-06-10 12:31:19
categories: writing
---
"""

from proselint.registry.checks import Check, CheckFlags, types

check_misplaced = Check(
    check_type=types.Existence(items=(r"et\. al", r"et\. al\.")),
    path="typography.punctuation.misplaced",
    message="Misplaced punctuation. It's 'et al.'",
)

check_exclamations_ppm = Check(
    check_type=types.ExistenceSimple(pattern=r"\w!"),
    path="typography.punctuation.exclamation",
    message="More than 30 ppm of exclamations. Keep them under control.",
    flags=CheckFlags(ppm_threshold=30),
)

check_hyperbole = Check(
    check_type=types.ExistenceSimple(pattern=r"\w*(?:!|\?){2,}"),
    path="typography.punctuation.hyperbole",
    message="'{}' is hyperbolic.",
)

check_spacing = Check(
    check_type=types.Consistency(term_pairs=((r"[\.\?!] \w", r"[\.\?!]  \w"),)),
    path="typography.punctuation.spacing",
    message="Inconsistent spacing after period (1 vs. 2 spaces).",
)

__register__ = (
    check_misplaced,
    check_exclamations_ppm,
    check_hyperbole,
    check_spacing,
)
