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
from proselint.tools import memoize, preferred_forms_check


@memoize
def check(text):
    """Suggest the preferred forms."""
    err = "MAU102"
    msg = "'{}' is the preferred form."

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
        ["convertible",       ["conversible"]],
        ["endow",             ["indow"]],
        ["enigmas",           ["enigmatas"]],
        ["eyeing",            ["eying"]],
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

        # Proper nouns
        ["Halloween",         ["haloween", "hallowe'en"]],
        ["Khrushchev",        ["Khruschev", "Kruschev"]],
        ["Ku Klux Klan",      ["Klu Klux Klan"]],
        ["Pontius Pilate",    ["Pontius Pilot"]],

        # Plurals
        ["sopranos",          ["soprani"]],

        # Misc. misspellings
        ["academically",      ["academicly"]],
        ["anilingus",         ["analingus"]],
        ["fluoride",          ["flouride"]],
        ["fluoridation",      ["flouridation"]],
        ["fluorescent",       ["flourescent"]],
        ["gist",              ["jist"]],
        ["glamour",           ["glamor"]],
        ["granddad",          ["grandad"]],
        ["grandpa",           ["granpa"]],
        ["highfalutin",       ["highfaluting", "highfalutin'", "hifalutin"]],
        ["financeable",       ["financable"]],
        ["praying mantis",    ["preying mantis"]],
        ["aren't i",          ["amn't i"]],
        ["aren't i",          ["an't i"]],
        ["spicy",             ["spicey"]],
        ["Hippocratic",       ["hypocratic"]],
        ["holistic",          ["wholistic"]],
        ["ideology",          ["idealogy"]],
        ["idiosyncrasy",      ["ideosyncracy"]],
        ["innovate",          ["inovate"]],
        ["inoculation",       ["innoculation", "inocculation"]],
        ["inundate",          ["innundate"]],
        ["inundated",         ["innundated"]],
        ["inundating",        ["innundating"]],
        ["inundates",         ["innundates"]],
        ["iridescent",        ["irridescent"]],
        ["kaleidoscope",      ["kaleidascope"]],
        ["knickknack",        ["knicknack"]],
        ["cummerbund",        ["kummerbund"]],
        ["lessor",            ["leasor"]],
        ["lessee",            ["leasee"]],
        ["liquefy",           ["liquify"]],
        ["loathsome",         ["loathesome"]],
        ["mademoiselle",      ["madamoiselle"]],
        ["jujitsu",           ["jiujutsu"]],
        ["minuscule",         ["miniscule"]],
        ["mischievous",       ["mischievious"]],
        ["occurred",          ["occured"]],
        ["plantar fasciitis", ["planter fasciitis", "plantar fascitis"]],
        ["pledgeable",        ["pledgable", "pledgeble"]],
        ["portentous",        ["portentuous", "portentious"]],
        ["preestablished",    ["prestablished"]],
        ["preexisting",       ["prexisting"]],
        ["presumptuous",      ["presumptious"]],
        ["remuneration",      ["renumeration"]],
        ["restaurateur",      ["restauranteur"]],
        ["stupefy",           ["stupify"]],
        ["subtly",            ["subtley"]],

        # Hyphenated words
        ["tortfeasor",        ["tort feasor", "tort-feasor"]],
        ["transship",         ["tranship", "trans-ship"]],
        ["transshipped",      ["transhipped", "trans-shipped"]],
        ["transshipping",     ["transhipping", "trans-shipping"]],
        ["long-standing",     ["longstanding"]],
        # ["longtime",         ["long time"]],

        # able vs. ible
        ["addable",           ["addible"]],
        ["adducible",         ["adduceable"]],
        ["impermissible",     ["impermissable"]],
        ["inadmissible",      ["inadmissable"]],
        ["inculcatable",      ["inculcatible"]],

        # er vs. or
        ["abettor",           ["abbeter"]],
        ["acquirer",          ["acquiror"]],
        ["promoter",          ["promotor"]],
        ["reckless",          ["wreckless"]],

        # Misc
        ["musical revue",     ["musical review"]],
        ["shoo-in",           ["shoe-in"]],

        # TODO, entries that are a bit complicated
        # announce
    ]

    return preferred_forms_check(text, preferences, err, msg)
