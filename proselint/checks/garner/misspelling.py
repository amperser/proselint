# -*- coding: utf-8 -*-
"""MAU102: Misspellings.

---
layout:     post
error_code: MAU102
source:     Garner's Modern American Usage
source_url: http://amzn.to/15wF76r
title:      misspellings
date:       2014-06-10 12:31:19
categories: writing
---

Points out misspellings.

"""
from proselint.tools import memoize, preferred_forms_check


@memoize
def check(text):
    """Suggest the preferred forms."""
    err = "MAU102"
    msg = "Misspelling. '{}' is the preferred form."

    misspellings = [

        ["academically",      ["academicly"]],
        ["anilingus",         ["analingus"]],
        ["fluoride",          ["flouride"]],
        ["fluoridation",      ["flouridation"]],
        ["fluorescent",       ["flourescent"]],
        ["forswear",          ["foreswear"]],
        ["free rein",         ["free reign"]],
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
        ["hirable",           ["hireable"]],
        ["holistic",          ["wholistic"]],
        ["ideology",          ["idealogy"]],
        ["idiosyncrasy",      ["ideosyncracy"]],
        ["improvise",         ["improvize"]],
        ["incurrence",        ["incurment"]],
        ["inevitability",     ["inevitableness"]],
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
        ["newsstand",         ["newstand"]],
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
        ["foreclose",         ["forclose"]],
    ]

    return preferred_forms_check(text, misspellings, err, msg)
