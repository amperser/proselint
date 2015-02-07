# -*- coding: utf-8 -*-
"""MAU102: Preferred forms, needless variants.

---
layout:     post
error_code: MAU102
source:     Garner's Modern American Usage
source_url: http://amzn.to/15wF76r
title:      abbetor
date:       2014-06-10 12:31:19
categories: writing
---

Points out use of needless variants and less preferred forms.

"""
import re
from proselint.tools import memoize


@memoize
def check(text):
    """Suggest the preferred forms."""
    err = "MAU102"
    msg = "{} is the preferred form."

    preferences = [

        # Needless variants
        ["abbreviable",      ["abbreviatable"]],
        ["abolition",        ["abolishment"]],
        ["accessory",        ["accessary"]],
        ["accrual",          ["accruement"]],
        ["accumulate",       ["cumulate"]],
        ["accused",          ["accusee"]],
        ["acquaintance",     ["acquaintanceship"]],
        ["acquittal",        ["acquitment"]],
        ["administer",       ["administrate"]],
        ["administered",     ["administrated"]],
        ["administering",    ["administrating"]],
        ["adulterous",       ["adulterate"]],
        ["advisory",         ["advisatory"]],
        ["advocate",         ["advocator"]],
        ["alleger",          ["allegator"]],
        ["allusive",         ["allusory"]],
        ["ameliorate",       ["meliorate"]],
        ["amorous",          ["amative"]],
        ["amortization",     ["amortizement"]],
        ["amphibology",      ["amphiboly"]],
        ["anachronism",      ["parachronism"]],
        ["anecdotist",       ["anecdotalist"]],
        ["anilingus",        ["anilinctus"]],
        ["anticipatory",     ["anticipative"]],
        ["convertible",      ["conversible"]],
        ["endow",            ["indow"]],
        ["enigmas",          ["enigmatas"]],
        ["eyeing",           ["eying"]],
        ["neglectful",       ["neglective"]],
        ["precedence",       ["precedency"]],
        ["preceptorial",     ["preceptoral"]],
        ["transposition",    ["transposal"]],
        ["precipitate",      ["precipitant"]],
        ["precipitancy",     ["precipitance"]],

        # Misc. misspellings
        ["academically",     ["academicly"]],
        ["anilingus",        ["analingus"]],
        ["praying mantis",   ["preying mantis"]],
        ["aren't i",         ["amn't i"]],
        ["aren't i",         ["an't i"]],

        # Hyphenated words
        ["tortfeasor",       ["tort feasor", "tort-feasor"]],
        ["transship",        ["tranship", "trans-ship"]],
        ["transshipped",     ["transhipped", "trans-shipped"]],
        ["transshipping",    ["transhipping", "trans-shipping"]],

        # able vs. ible
        ["addable",          ["addible"]],
        ["adducible",        ["adduceable"]],

        # er vs. or
        ["abettor",          ["abbeter"]],
        ["acquirer",         ["acquiror"]],

        # TODO, entries that are a bit complicated
        # announce
    ]
    errors = []
    for p in preferences:
        for r in p[1]:
            for m in re.finditer("\s{}\s".format(r), text, flags=re.IGNORECASE):
                errors.append((m.start()+1, m.end(), err, msg.format(p[0])))

    return errors
