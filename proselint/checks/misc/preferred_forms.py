# -*- coding: utf-8 -*-
"""Preferred forms.

---
layout:     post
source:     Garner's Modern American Usage
source_url: http://bit.ly/1T4alrY
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
    err = "garner.preferred_forms"
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
        ["hippopotamuses",      ["hippopotami"]],
        ["manifestos",          ["manifesti"]],
        # ["matrixes",            ["matrices"]],
        ["mongooses",           ["mongeese"]],
        ["narcissi",            ["narcissuses"]],
        ["retinas",             ["retinae"]],
        ["sopranos",            ["soprani"]],
        ["titmice",             ["titmouses"]],

        # Hyphenated words
        ["long-standing",       ["longstanding"]],
        ["sans serif",          ["sans-serif", "sanserif"]],
        ["tortfeasor",          ["tort feasor", "tort-feasor"]],
        ["transship",           ["tranship", "trans-ship"]],
        ["transshipped",        ["transhipped", "trans-shipped"]],
        ["transshipping",       ["transhipping", "trans-shipping"]],
        ["non sequitur",        ["non-sequitur"]],

        # Misc
        ["attitude",            ["mental attitude"]],
        ["Chief Justice of the United States",
            ["Chief Justice of the United States Supreme Court",
             "Chief Justice of the Supreme Court of the United States."]],
        ["chitterlings",        ["chitlings", "chitlins"]],
        ["combustion engine",   ["combustible engine"]],
        ["during / throughout", ["for the duration of"]],
        ["foreclose on",        ["foreclose againt"]],
        ["friend in common",    ["mutual friend"]],
        ["in regard to",        ["in regards to"]],
        ["infectious",          ["infectuous"]],
        ["inferable",           ["inferrable", "inferrible"]],
        ["knowing that",        ["in light of the fact that"]],
        ["lanyard",             ["laniard"]],
        ["largess",             ["largesse"]],
        ["lasagna",             ["lasagne"]],
        ["leery",               ["leary"]],
        ["lend me her",         ["loan me her"]],
        ["lend me his",         ["loan me his"]],
        ["lend me their",       ["loan me their"]],
        ["lend me your",        ["loan me your"]],
        ["lent me her",         ["loaned me her"]],
        ["lent me his",         ["loaned me his"]],
        ["lent me their",       ["loaned me their"]],
        ["lent me your",        ["loaned me your"]],
        ["linguist",            ["linguistician"]],
        ["matzo-ball",          ["matzoh-ball",
                                 "matza-ball",
                                 "matzah-ball",
                                 "matsah-ball"]],
        ["mayoralty",           ["mayorality"]],
        ["mealy-mouthed",       ["mealymouthed"]],
        ["mean-spirited",       ["meanspirited"]],
        ["midwifed",            ["midwived"]],
        ["moniker",             ["monicker"]],
        ["musical revue",       ["musical review"]],
        ["mustache",            ["moustache"]],
        ["nonplussed",          ["nonplused"]],
        ["nonplussing",         ["nonplusing"]],
        ["non sequitur",        ["nonsequitur"]],
        ["not nearly as",       ["nowhere near as"]],
        ["off",                 ["off of"]],
        ["podiatrist",          ["chiropodist"]],
        ["podiatry",            ["chiropody"]],
        ["shoo-in",             ["shoe-in"]],
        ["suicide",             ["suicide victim"]],
        ["the highway median",  ["the highway medium"]],
        ["vaipidity",           ["vapidness"]],
        ["weather vane",        ["weather vein", "weather vain"]],
        ["with regard to",      ["with regards to"]],

        # Idioms
        ["a couple of people",  ["a couple people"]],
        ["all the time",        ["all of the time"]],
        ["as follows",          ["as follow"]],
        ["bulk large",          ["bulk largely"]],
        ["burying the lede",    ["burying the lead"]],
        ["came to naught",      ["came to nought"]],
        ["come off it",         ["come off of it"]],
        ["corroborating evidence", ["corroborative evidence"]],
        ["dear departed",       ["dearly departed"]],
        ["default on a loan",   ["default to a loan"]],
        ["draw an inference",   ["make an inference"]],
        ["in the meantime",     ["in the meanwhile"]],
        ["long distances",      ["lengthy distances"]],
        ["madding crowd",       ["maddening crowd"]],
        ["Magna Carta",         ["Magna Charta"]],
        ["marriage of convenience", ["mariage de convenance"]],
        ["Meanwhile,",          ["Meantime,"]],
        ["Midwest",             ["Middle West"]],
        ["Midwestern",          ["Middle Western"]],
        ["modi operandi",       ["modes of operandi"]],
        ["modus operandi",      ["mode of operandi"]],
        ["motion seconded",     ["notion seconded"]],
        ["mucous membranes",    ["mucus membranes"]],
        ["must pass muster",    ["must past muster"]],
        ["neck-and-neck",       ["neck-in-neck"]],
        ["no-holds-barred",     ["no-holes-barred"]],
        ["oil magnate",         ["oil magnet"]],
        ["punch up the lede",   ["punch up the lead"]],
        ["railroad magnate",    ["railroad magnet"]],
        ["seconded the motion", ["seconded the notion"]],
        ["statute of limitationas", ["statute of limits"]],
        ["take precedence over", ["take prescience over"]],
        ["the last two",        ["both of the last two"]],
        ["the last two",        ["both of the last"]],
        ["unorganic food",      ["inorganic food"]],
        ["vale of tears",       ["veil of tears"]],
        ["Venus flytrap",       ["Venus's flytrap", "Venus' flytrap"]],
        ["was accused of",      ["was accused with"]],

        # Verbosity
        ["try to",              ["make an attempt to"]],
        ["try to",              ["make attempts to"]],
        ["try to",              ["make efforts to"]],
        ["tried to",            ["made an attempt to"]],
        ["tried to",            ["made attempts to"]],
        ["tried to",            ["made efforts to"]],
        ["modern",              ["modern-day"]],

        # Grammar
        ["be misled",           ["be mislead"]],
        ["was misled",          ["was mislead"]],
        ["were misled",         ["were mislead"]],

        # Euphemisms
        ["a search-and-destroy mission", ["armed reconnaissance"]],
        ["abortion",            ["pregnancy termination"]],
        ["bisexual",            ["sexually ambidextrous"]],
        ["exterminator",        ["extermination engineer"]],
        ["firing",              ["permanent layoff"]],
        ["rat-catcher",         ["rodent operative"]],

        # Tenses
        ["mistook",             ["mistaked"]],

        # Accents
        ["né",                  ["ne"]],
        ["née",                 ["nee"]],
    ]

    return preferred_forms_check(text, preferences, err, msg)
