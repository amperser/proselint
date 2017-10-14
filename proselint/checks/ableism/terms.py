# -*- coding: utf-8 -*-
"""Ableism.

---
layout:     post
source:     Autistic Hoya: Ableism/Language
source_url: http://www.autistichoya.com/p/ableist-words-and-terms-to-avoid.html
title:      Ableism
date:       2017-09-14
categories: writing
---

Warns about potentially ableist language and slang.

"""
from proselint.tools import existence_check, memoize


@memoize
def check(text):
    """Check the text."""
    err = "ableism.terms"
    msg = u"""'{}' is potentially an ableist term. Consider the context and find
             some other way to say it."""

    list = [
        # "add", FIXME use topic detetor to decide whether "add" is offensive
        "autism",
        "autistic",
        "blind",
        "bound",
        "deaf",
        "deaf and dumb",
        "deaf mute",
        "deformed",
        "delusional",
        "derp",
        "diffability",
        "differently abled",
        "different abilities",
        "dim",
        "dim witted",
        "epileptic",
        "fit",
        "feeble",
        "feeble mind",
        "feeble minded",
        "handicap",
        "handicapped",
        "handicapable",
        "harelip",
        "hare lip",
        "hearing impaired",
        "hermaphrodite",
        "herp derp",
        "incapacitated",
        "invalid",
        "mad",
        "madhouse",
        "madman",
        "manic",
        "mental",
        "mentally defective",
        "mentally deficient",
        "morbidly obese",
        "obese",
        "nuts",
        "nutter",
        "slow",
        "special",
        "specially abled",
        "special needs",
        "suffers from",
        "sufferer",
        "suffering",
        "the disabled",
        "weak",
        "wheelchair bound",
        "yuppie flu"
    ]
    list = [term.replace(" ","[ -]") for term in list]

    return existence_check(text, ableism, err, msg)
