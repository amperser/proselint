# -*- coding: utf-8 -*-
"""MAU102: Needless variants.

---
layout:     post
error_code: MAU102
source:     Garner's Modern American Usage
source_url: http://amzn.to/15wF76r
title:      needless variants
date:       2014-06-10 12:31:19
categories: writing
---

Points out use of needless variants.

"""
from proselint.tools import memoize, preferred_forms_check


@memoize
def check(text):
    """Suggest the preferred forms."""
    err = "MAU102"
    msg = "Needless variant. '{}' is the preferred form."

    preferences = [

        # Needless variants
        ["abbreviable",       ["abbreviatable"]],
        ["abolition",         ["abolishment"]],
        ["accessory",         ["accessary"]],
        ["accrual",           ["accruement"]],
        ["accumulate",        ["cumulate"]],
        ["accused",           ["accusee"]],
        ["acquaintance",      ["acquaintanceship"]],
        ["acquittal",         ["acquitment"]],
        ["administer",        ["administrate"]],
        ["administered",      ["administrated"]],
        ["administering",     ["administrating"]],
        ["adulterous",        ["adulterate"]],
        ["advisory",          ["advisatory"]],
        ["advocate",          ["advocator"]],
        ["alleger",           ["allegator"]],
        ["allusive",          ["allusory"]],
        ["ameliorate",        ["meliorate"]],
        ["amorous",           ["amative"]],
        ["amortization",      ["amortizement"]],
        ["amphibology",       ["amphiboly"]],
        ["anachronism",       ["parachronism"]],
        ["anecdotist",        ["anecdotalist"]],
        ["anilingus",         ["anilinctus"]],
        ["anticipatory",      ["anticipative"]],
        ["buck naked",        ["butt naked"]],
        ["convertible",       ["conversible"]],
        ["catch fire",        ["catch on fire"]],
        ["ceasefire",         ["cease fire"]],
        ["cellphone",         ["cell phone", "cell-phone"]],
        ["endow",             ["indow"]],
        ["enigmas",           ["enigmatas"]],
        ["eyeing",            ["eying"]],
        ["henceforth",        ["henceforward"]],
        ["expedient",         ["expediential"]],
        ["hesitancy",         ["hesitance"]],
        ["heterogeneous",     ["heterogenous"]],
        ["hierarchical",      ["hierarchic"]],
        ["hindmost",          ["hindermost"]],
        ["honoree",           ["honorand"]],
        ["hypostatize",       ["hypostasize"]],
        ["hysterical",        ["hysteric"]],
        ["idolize",           ["idolatrize"]],
        ["impersonation",     ["personation"]],
        ["impervious",        ["imperviable"]],
        ["importunity",       ["importunacy"]],
        ["impotence",         ["impotency"]],
        ["imprimatur",        ["imprimatura"]],
        ["incitement",        ["incitation"]],
        ["inconsistency",     ["inconsistence"]],
        ["incriminate",       ["criminate"]],
        ["incurrence",        ["incurment"]],
        ["neglectful",        ["neglective"]],
        ["precedence",        ["precedency"]],
        ["preceptorial",      ["preceptoral"]],
        ["transposition",     ["transposal"]],
        ["precipitate",       ["precipitant"]],
        ["precipitancy",      ["precipitance"]],
        ["kaffeeklatsch",     ["Coffee klatsch", "coffee klatch"]],
        ["knickknack",        ["nicknack"]],
        ["movable",           ["moveable"]],
        ["murk",              ["mirk"]],
        ["murky",             ["mirky"]],
        ["password",          ["passcode"]],
        ["pederast",          ["paederast"]],
        ["pejorative",        ["perjorative"]],
        ["succubus",          ["succuba"]],
    ]

    return preferred_forms_check(text, preferences, err, msg)
