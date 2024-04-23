"""Misspellings.

---
layout:     post
source:     Garner's Modern American Usage
source_url: http://bit.ly/1T4alrY
title:      misspellings
date:       2014-06-10
categories: writing
---

Points out misspellings.

"""
from __future__ import annotations

from proselint.checks import Pd
from proselint.checks import CheckResult
from proselint.checks import preferred_forms_check_opti

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = ["I like this alot.", "I stay 'til sundown."]


def check(text: str) -> list[CheckResult]:
    """Suggest the preferred forms."""
    err = "spelling.misc"
    msg = "Misspelling. '{}' is the preferred spelling."

    items: dict[str, str] = {
        "alot": "a lot",
        "accomodatable": "accommodable",
        "analingus": "anilingus",
        "amn't i": "aren't i",
        "an't i": "aren't i",
        "bob wire": "barbed wire",
        "chargable": "chargeable",
        "chiffonnier": "chiffonier",
        "chinchy": "chintzy",
        "chipolte": "chipotle",
        "chlorophyl": "chlorophyll",
        "chocolatey": "chocolaty",
        "chronical": "chronicle",
        "chronicals": "chronicles",
        "coldslaw": "coleslaw",
        "choosey": "choosy",
        "kummerbund": "cummerbund",
        "financable": "financeable",
        "flourescent": "fluorescent",
        "flouridation": "fluoridation",
        "flouride": "fluoride",
        "forclose": "foreclose",
        "foreswear": "forswear",
        "free reign": "free rein",
        "jist": "gist",
        "glamor": "glamour",
        "grandad": "granddad",
        "granpa": "grandpa",
        "hypocratic": "Hippocratic",
        "hireable": "hirable",
        "wholistic": "holistic",
        "idealogy": "ideology",
        "ideosyncracy": "idiosyncrasy",
        "improvize": "improvise",
        "incurment": "incurrence",
        "inevitableness": "inevitability",
        "inovate": "innovate",
        "innoculation": "inoculation",
        "inocculation": "inoculation",
        "intergral": "integral",
        "innundate": "inundate",
        "innundated": "inundated",
        "innundates": "inundates",
        "innundating": "inundating",
        "irridescent": "iridescent",
        "irrevelant": "irrelevant",
        "jiujutsu": "jujitsu",
        "kaleidascope": "kaleidoscope",
        "knicknack": "knickknack",
        "lassoes": "lassos",
        "leasee": "lessee",
        "leasor": "lessor",
        "liason": "liaison",
        "laison": "liaison",
        "lightening rod": "lightning rod",
        "struck by lightening": "struck by lightning",
        "liquify": "liquefy",
        "loathesome": "loathsome",
        "loadstar": "lodestar",
        "to make due": "to make do",
        "madamoiselle": "mademoiselle",
        "marshall arts": "martial arts",
        "court marshall": "court-martial",
        "court-marshall": "court-martial",
        "maelstorm": "maelstrom",
        "maffia": "mafia",
        "mafiosos": "mafiosi",
        "mangos": "mangoes",
        "marihuana": "marijuana",
        "marshmellow": "marshmallow",
        "marshall law": "martial law",
        "massacering": "massacring",
        "massacreing": "massacring",
        "measels": "measles",
        "momento": "memento",
        "miniscule": "minuscule",
        "milage": "mileage",
        "mileau": "milieu",
        "millenium": "millennium",
        "millenia": "millennia",
        "milleniums": "millenniums",
        "millepede": "millipede",
        "millionnaire": "millionaire",
        "milktoast": "milquetoast",
        "mimiced": "mimicked",
        "mimicing": "mimicking",
        "mispelling": "misspelling",
        "mischievious": "mischievous",
        "mocasin": "moccasin",
        "moccassin": "moccasin",
        "mocassin": "moccasin",
        "monolog": "monologue",
        "monologist": "monologuist",
        "naptha": "naphtha",
        "naval orange": "navel orange",
        "neckware": "neckwear",
        "newstand": "newsstand",
        "non sequiter": "non sequitur",
        "non sequitar": "non sequitur",
        "non sequitor": "non sequitur",
        "nouveau rich": "nouveau riche",
        "occured": "occurred",
        "of-the-shelf": "off-the-shelf",
        "planter fasciitis": "plantar fasciitis",
        "plantar fascitis": "plantar fasciitis",
        "pledgable": "pledgeable",
        "pledgeble": "pledgeable",
        "portentuous": "portentous",
        "portentious": "portentous",
        "preying mantis": "praying mantis",
        "prestablished": "preestablished",
        "prexisting": "preexisting",
        "presumptious": "presumptuous",
        "rarify": "rarefy",
        "wreckless": "reckless",
        "renumeration": "remuneration",
        "restauranteur": "restaurateur",
        "revery": "reverie",
        "spicey": "spicy",
        "stupify": "stupefy",
        "subtley": "subtly",
        "tenderbox": "tinderbox",
        "tympani": "timpani",
        "a timpano": "a timpani",
        "umteenth": "umpteenth",
        "verbage": "verbiage",
    }

    return preferred_forms_check_opti(text, items, err, msg)


def check_special(text: str) -> list[CheckResult]:
    """Suggest the preferred forms."""
    err = "spelling.misc"
    msg = "Misspelling. '{}' is the preferred spelling."

    items: dict[str, str] = {
        "highfaluting": "highfalutin",
        "highfalutin'": "highfalutin",
        "hifalutin": "highfalutin",
        "'till": "till",
        "'til": "till",
    }

    return preferred_forms_check_opti(text, items, err, msg, padding=Pd.sep_in_txt)
