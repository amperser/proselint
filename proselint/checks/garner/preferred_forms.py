# -*- coding: utf-8 -*-
"""MAU102: Preferred forms.

---
layout:     post
error_code: MAU102
source:     Garner's Modern American Usage
source_url: http://amzn.to/15wF76r
title:      preferred forms
date:       2014-06-10 12:31:19
categories: writing
---

Points out preferred forms.

"""
from proselint.tools import memoize, preferred_forms_check


@memoize
def check(text):
    """Suggest the preferred forms."""
    err = "MAU102"
    msg = "'{}' is the preferred form."

    preferences = [

        # Obsolete words
        ["imprimatur",          ["imprimature"]],

        # Proper nouns
        ["Halloween",           ["haloween", "hallowe'en"]],
        ["Khrushchev",          ["Khruschev", "Kruschev"]],
        ["Ku Klux Klan",        ["Klu Klux Klan"]],
        ["Pontius Pilate",      ["Pontius Pilot"]],

        # Plurals
        ["sopranos",            ["soprani"]],
        ["hippopotamuses",      ["hippopotami"]],
        ["titmice",             ["titmouses"]],
        ["retinas",             ["retinae"]],

        # Hyphenated words
        ["tortfeasor",          ["tort feasor", "tort-feasor"]],
        ["transship",           ["tranship", "trans-ship"]],
        ["transshipped",        ["transhipped", "trans-shipped"]],
        ["transshipping",       ["transhipping", "trans-shipping"]],
        ["long-standing",       ["longstanding"]],
        # ["longtime",           ["long time"]],

        # er vs. or
        ["abductor",            ["abducter"]],
        ["abettor",             ["abbeter"]],
        ["acquirer",            ["acquiror"]],
        ["adapter",             ["adaptor"]],
        ["collector",           ["collecter"]],
        ["conjurer",            ["conjuror"]],
        ["corrupter",           ["corruptor"]],
        ["digester",            ["digestor"]],
        ["dispenser",           ["dispensor"]],
        ["distributor",         ["distributer"]],
        ["endorser",            ["endorsor"]],
        ["eraser",              ["erasor"]],
        ["idolater",            ["idolator"]],
        ["impostor",            ["imposter"]],
        ["infiltrator",         ["infiltrater"]],
        ["investor",            ["invester"]],
        ["manipulator",         ["manipulater"]],
        ["persecutor",          ["persecuter"]],
        ["promoter",            ["promotor"]],
        ["promoter",            ["promotor"]],
        ["purveyor",            ["purveyer"]],
        ["requester",           ["requestor"]],
        ["reviser",             ["revisor"]],
        ["surveyor",            ["surveyer"]],

        # in vs. un
        ["inadvisable",         ["unadvisable"]],
        ["inalienable",         ["unalienable"]],
        ["inexpressive",        ["unexpressive"]],
        ["infeasible",          ["unfea"]],

        # Misc
        ["musical revue",       ["musical review"]],
        ["shoo-in",             ["shoe-in"]],
        ["foreclose on",        ["foreclose againt"]],
        ["during / throughout", ["for the duration of"]],

        # TODO, entries that are a bit complicated
        # announce
    ]

    return preferred_forms_check(text, preferences, err, msg)


@memoize
def check_able_ible(text):
    """-able vs. -ible."""

    err = "MAU102"
    msg = "-able vs. -ible. '{}' is the preferred form."

    preferences = [

        ["actionable",      ["actionible"]],
        ["addable",         ["addible"]],
        ["admittable",      ["admittible"]],
        ["advisable",       ["advisible"]],
        ["affectable",      ["affectible"]],
        ["allegeable",      ["allegeible"]],
        ["analyzable",      ["analyzible"]],
        ["annexable",       ["annexible"]],
        ["arrestable",      ["arrestible"]],
        ["ascendable",      ["ascendible"]],
        ["assertable",      ["assertible"]],
        ["assessable",      ["assessible"]],
        ["averageable",     ["averageible"]],
        ["bailable",        ["bailible"]],
        ["blamable",        ["blamible"]],
        ["changeable",      ["changeible"]],
        ["chargeable",      ["chargeible"]],
        ["circumscribable", ["circumscribible"]],
        ["commensurable",   ["commensurible"]],
        ["committable",     ["committible"]],
        ["condensable",     ["condensible"]],
        ["connectable",     ["connectible"]],
        ["contestable",     ["contestible"]],
        ["contractable",    ["contractible"]],
        ["conversable",     ["conversible"]],
        ["convictable",     ["convictible"]],
        ["correctable",     ["correctible"]],
        ["definable",       ["definible"]],
        ["detectable",      ["detectible"]],
        ["diagnosable",     ["diagnosible"]],
        ["discussable",     ["discussible"]],
        ["endorsable",      ["endorsible"]],
        ["enforceable",     ["enforceible"]],
        ["evadable",        ["evadible"]],
        ["excisable",       ["excisible"]],
        ["excludable",      ["excludible"]],
        ["expandable",      ["expandible"]],
        ["extendable",      ["extendible"]],
        ["extractable",     ["extractible"]],
        ["ignitable",       ["ignitible"]],
        ["immovable",       ["immovible"]],
        ["improvable",      ["improvible"]],
        ["includable",      ["includible"]],
        ["inferable",       ["inferible"]],
        ["inventable",      ["inventible"]],
        ["investable",      ["investible"]],
        ["lapsable",        ["lapsible"]],
        ["lovable",         ["lovible"]],
        ["mixable",         ["mixible"]],
        ["movable",         ["movible"]],
        ["noticeable",      ["noticeible"]],
        ["offendable",      ["offendible"]],
        ["patentable",      ["patentible"]],
        ["persuadable",     ["persuadible"]],
        ["preventable",     ["preventible"]],
        ["processable",     ["processible"]],
        ["protectable",     ["protectible"]],
        ["ratable",         ["ratible"]],
        ["redressable",     ["redressible"]],
        ["referable",       ["referible"]],
        ["retractable",     ["retractible"]],
        ["revisable",       ["revisible"]],
        ["rinsable",        ["rinsible"]],
        ["salable",         ["salible"]],
        ["suspendable",     ["suspendible"]],
        ["tractable",       ["tractible"]],
        ["transferable",    ["transferible"]],
        ["transmittable",   ["transmittible"]],
        ["willable",        ["willible"]],

        ["accessible",      ["accessable"]],
        ["adducible",       ["adducable"]],
        ["admissible",      ["admissable"]],
        ["audible",         ["audable"]],
        ["avertible",       ["avertable"]],
        ["collapsible",     ["collapsable"]],
        ["collectible",     ["collectable"]],
        ["combustible",     ["combustable"]],
        ["compactible",     ["compactable"]],
        ["compatible",      ["compatable"]],
        ["comprehensible",  ["comprehensable"]],
        ["compressible",    ["compressable"]],
        ["concussible",     ["concussable"]],
        ["conductible",     ["conductable"]],
        ["contemptible",    ["contemptable"]],
        ["controvertible",  ["controvertable"]],
        ["convertible",     ["convertable"]],
        ["corrodible",      ["corrodable"]],
        ["corruptible",     ["corruptable"]],
        ["credible",        ["credable"]],
        ["deducible",       ["deducable"]],
        ["deductible",      ["deductable"]],
        ["defeasible",      ["defeasable"]],
        ["defensible",      ["defensable"]],
        ["descendible",     ["descendable"]],
        ["destructible",    ["destructable"]],
        ["diffusible",      ["diffusable"]],
        ["digestible",      ["digestable"]],
        ["discernible",     ["discernable"]],
        ["dismissible",     ["dismissable"]],
        ["divisible",       ["divisable"]],
        ["edible",          ["edable"]],
        ["educible",        ["educable"]],
        ["eligible",        ["eligable"]],
        ["erodible",        ["erodable"]],
        ["exhaustible",     ["exhaustable"]],
        ["expressible",     ["expressable"]],
        ["fallible",        ["fallable"]],
        ["feasible",        ["feasable"]],
        ["flexible",        ["flexable"]],
        ["forcible",        ["forcable"]],
        ["fusible",         ["fusable"]],
        ["gullible",        ["gullable"]],
        ["horrible",        ["horrable"]],
        ["impressible",     ["impressable"]],
        ["incorrigible",    ["incorrigable"]],
        ["indelible",       ["indelable"]],
        ["intelligible",    ["intelligable"]],
        ["interfusible",    ["interfusable"]],
        ["invincible",      ["invincable"]],
        ["irascible",       ["irascable"]],
        ["irresistible",    ["irresistable"]],
        ["legible",         ["legable"]],
        ["negligible",      ["negligable"]],
        ["omissible",       ["omissable"]],
        ["oppressible",     ["oppressable"]],
        ["ostensible",      ["ostensable"]],
        ["perceptible",     ["perceptable"]],
        ["perfectible",     ["perfectable"]],
        ["permissible",     ["permissable"]],
        ["plausible",       ["plausable"]],
        ["possible",        ["possable"]],
        ["producible",      ["producable"]],
        ["reducible",       ["reducable"]],
        ["remissible",      ["remissable"]],
        ["reprehensible",   ["reprehensable"]],
        ["repressible",     ["repressable"]],
        ["resistible",      ["resistable"]],
        ["responsible",     ["responsable"]],
        ["reversible",      ["reversable"]],
        ["revertible",      ["revertable"]],
        ["risible",         ["risable"]],
        ["seducible",       ["seducable"]],
        ["sensible",        ["sensable"]],
        ["submersible",     ["submersable"]],
        ["submergible",     ["submergable"]],
        ["suggestible",     ["suggestable"]],
        ["suppressible",    ["suppressable"]],
        ["susceptible",     ["susceptable"]],
        ["terrible",        ["terrable"]],
        ["transfusible",    ["transfusable"]],
        ["transmissible",   ["transmissable"]],
        ["uncollectible",   ["uncollectable"]],
        ["vendible",        ["vendable"]],
        ["visible",         ["visable"]]
    ]

    return preferred_forms_check(text, preferences, err, msg)
