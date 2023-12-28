"""Misspellings.

---
layout:     post
source:     Garner's Modern American Usage
source_url: http://bit.ly/1T4alrY
title:      misspellings
date:       2014-06-10 12:31:19
categories: writing
---

Points out misspellings.

"""
from __future__ import annotations

from proselint.tools import ResultCheck, memoize, preferred_forms_check


@memoize
def check(text: str) -> list[ResultCheck]:
    """Suggest the preferred forms."""
    err = "spelling.misc"
    msg = "Misspelling. '{}' is the preferred spelling."

    misspellings = [
        ["a lot",             ["alot"]],
        ["accommodable",      ["accomodatable"]],
        ["anilingus",         ["analingus"]],
        ["aren't i",          ["amn't i"]],
        ["aren't i",          ["an't i"]],
        ["barbed wire",       ["bob wire"]],
        ["chargeable",        ["chargable"]],
        ["chiffonier",        ["chiffonnier"]],
        ["chintzy",           ["chinchy"]],
        ["chipotle",          ["chipolte"]],
        ["chlorophyll",       ["chlorophyl"]],
        ["chocolaty",         ["chocolatey"]],
        ["chronicle",         ["chronical"]],
        ["chronicles",        ["chronicals"]],
        ["coleslaw",          ["coldslaw"]],
        ["choosy",            ["choosey"]],
        ["cummerbund",        ["kummerbund"]],
        ["financeable",       ["financable"]],
        ["fluorescent",       ["flourescent"]],
        ["fluoridation",      ["flouridation"]],
        ["fluoride",          ["flouride"]],
        ["foreclose",         ["forclose"]],
        ["forswear",          ["foreswear"]],
        ["free rein",         ["free reign"]],
        ["gist",              ["jist"]],
        ["glamour",           ["glamor"]],
        ["granddad",          ["grandad"]],
        ["grandpa",           ["granpa"]],
        ["highfalutin",       ["highfaluting", "highfalutin'", "hifalutin"]],
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
        ["integral",          ["intergral"]],
        ["inundate",          ["innundate"]],
        ["inundated",         ["innundated"]],
        ["inundates",         ["innundates"]],
        ["inundating",        ["innundating"]],
        ["iridescent",        ["irridescent"]],
        ["irrelevant",        ["irrevelant"]],
        ["jujitsu",           ["jiujutsu"]],
        ["kaleidoscope",      ["kaleidascope"]],
        ["knickknack",        ["knicknack"]],
        ["lassos",            ["lassoes"]],
        ["lessee",            ["leasee"]],
        ["lessor",            ["leasor"]],
        ["liaison",           ["liason"]],
        ["liaison",           ["laison"]],
        ["lightning rod",     ["lightening rod"]],
        ["struck by lightning", ["struck by lightening"]],
        ["liquefy",           ["liquify"]],
        ["loathsome",         ["loathesome"]],
        ["lodestar",          ["loadstar"]],
        ["to make do",        ["to make due"]],
        ["mademoiselle",      ["madamoiselle"]],
        ["martial arts",      ["marshall arts"]],
        ["court-martial",     ["court marshall", "court-marshall"]],
        ["maelstrom",         ["maelstorm"]],
        ["mafia",             ["maffia"]],
        ["mafiosi",           ["mafiosos"]],
        ["mangoes",           ["mangos"]],
        ["marijuana",         ["marihuana"]],
        ["marshmallow",       ["marshmellow"]],
        ["martial law",       ["marshall law"]],
        ["massacring",        ["massacering", "massacreing"]],
        ["measles",           ["measels"]],
        ["memento",           ["momento"]],
        ["minuscule",         ["miniscule"]],
        ["mileage",           ["milage"]],
        ["milieu",            ["mileau"]],
        ["millennium",        ["millenium"]],
        ["millennia",         ["millenia"]],
        ["millenniums",       ["milleniums"]],
        ["millipede",         ["millepede"]],
        ["millionaire",       ["millionnaire"]],
        ["milquetoast",       ["milktoast"]],
        ["mimicked",          ["mimiced"]],
        ["mimicking",         ["mimicing"]],
        ["misspelling",       ["mispelling"]],
        ["mischievous",       ["mischievious"]],
        ["moccasin",          ["mocasin", "moccassin", "mocassin"]],
        ["monologue",         ["monolog"]],
        ["monologuist",       ["monologist"]],
        ["naphtha",           ["naptha"]],
        ["navel orange",      ["naval orange"]],
        ["neckwear",          ["neckware"]],
        ["newsstand",         ["newstand"]],
        ["non sequitur",      ["non sequiter",
                               "non sequitar",
                               "non sequitor"]],
        ["nouveau riche",     ["nouveau rich"]],
        ["occurred",          ["occured"]],
        ["plantar fasciitis", ["planter fasciitis", "plantar fascitis"]],
        ["pledgeable",        ["pledgable", "pledgeble"]],
        ["portentous",        ["portentuous", "portentious"]],
        ["praying mantis",    ["preying mantis"]],
        ["preestablished",    ["prestablished"]],
        ["preexisting",       ["prexisting"]],
        ["presumptuous",      ["presumptious"]],
        ["rarefy",            ["rarify"]],
        ["reckless",          ["wreckless"]],
        ["remuneration",      ["renumeration"]],
        ["restaurateur",      ["restauranteur"]],
        ["reverie",           ["revery"]],
        ["spicy",             ["spicey"]],
        ["stupefy",           ["stupify"]],
        ["subtly",            ["subtley"]],
        ["till",              ["\'till?"]],
        ["tinderbox",         ["tenderbox"]],
        ["timpani",           ["tympani"]],
        ["a timpani",         ["a timpano"]],
        ["umpteenth",         ["umteenth"]],
        ["verbiage",          ["verbage"]],
    ]

    return preferred_forms_check(text, misspellings, err, msg)
