"""
Preferred forms.

---
layout:     post
source:     Garner's Modern American Usage
source_url: http://bit.ly/1T4alrY
title:      preferred forms
date:       2014-06-10
categories: writing
---

Points out preferred forms.

"""
from __future__ import annotations

from proselint.checks import CheckResult, preferred_forms_check_opti, registry

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "It was almost haloween.",
    "He is Chief Justice of the Supreme Court of the United States.",
]


def check(text: str) -> list[CheckResult]:
    """Suggest the preferred forms."""
    err = "misc.preferred_forms.garner"
    msg = "'{}' is the preferred form."

    items: dict[str, str] = {
        # Obsolete words
        "imprimature": "imprimatur",
        # Proper nouns
        "haloween": "Halloween",
        "hallowe'en": "Halloween",
        "Khruschev": "Khrushchev",
        "Kruschev": "Khrushchev",
        "Klu Klux Klan": "Ku Klux Klan",
        "Pontius Pilot": "Pontius Pilate",
        # Plurals
        "hippopotami": "hippopotamuses",
        "manifesti": "manifestos",
        # "matrices": "matrixes",
        "mongeese": "mongooses",
        "narcissuses": "narcissi",
        "retinae": "retinas",
        "soprani": "sopranos",
        "titmouses": "titmice",
        # Hyphenated words
        "longstanding": "long-standing",
        "sans-serif": "sans serif",
        "sanserif": "sans serif",
        "tort feasor": "tortfeasor",
        "tort-feasor": "tortfeasor",
        "tranship": "transship",
        "trans-ship": "transship",
        "transhipped": "transshipped",
        "trans-shipped": "transshipped",
        "transhipping": "transshipping",
        "trans-shipping": "transshipping",
        "non-sequitur": "non sequitur",
        # Misc
        "mental attitude": "attitude",
        "Chief Justice of the United States "
        "Supreme Court": "Chief Justice of the United States",
        "Chief Justice of the Supreme Court "
        "of the United States": "Chief Justice of the United States",
        "chitlings": "chitterlings",
        "chitlins": "chitterlings",
        "combustible engine": "combustion engine",
        "for the duration of": "during / throughout",
        "foreclose againt": "foreclose on",
        "mutual friend": "friend in common",
        "in regards to": "in regard to",
        "infectuous": "infectious",
        "inferrable": "inferable",
        "inferrible": "inferable",
        "in light of the fact that": "knowing that",
        "laniard": "lanyard",
        "largesse": "largess",
        "lasagne": "lasagna",
        "leary": "leery",
        "loan me her": "lend me her",
        "loan me his": "lend me his",
        "loan me their": "lend me their",
        "loan me your": "lend me your",
        "loaned me her": "lent me her",
        "loaned me his": "lent me his",
        "loaned me their": "lent me their",
        "loaned me your": "lent me your",
        "linguistician": "linguist",
        "matzoh-ball": "matzo-ball",
        "matza-ball": "matzo-ball",
        "matzah-ball": "matzo-ball",
        "matsah-ball": "matzo-ball",
        "mayorality": "mayoralty",
        "mealymouthed": "mealy-mouthed",
        "meanspirited": "mean-spirited",
        "midwived": "midwifed",
        "monicker": "moniker",
        "musical review": "musical revue",
        "moustache": "mustache",
        "nonplused": "nonplussed",
        "nonplusing": "nonplussing",
        "nonsequitur": "non sequitur",
        "nowhere near as": "not nearly as",
        "off of": "off",
        "chiropodist": "podiatrist",
        "chiropody": "podiatry",
        "shoe-in": "shoo-in",
        "suicide victim": "suicide",
        "the highway medium": "the highway median",
        "vapidness": "vaipidity",
        "weather vein": "weather vane",
        "weather vain": "weather vane",
        "with regards to": "with regard to",
        # Idioms
        "a couple people": "a couple of people",
        "all of the time": "all the time",
        "as follow": "as follows",
        "bulk largely": "bulk large",
        "burying the lead": "burying the lede",
        "came to nought": "came to naught",
        "come off of it": "come off it",
        "corroborative evidence": "corroborating evidence",
        "dearly departed": "dear departed",
        "default to a loan": "default on a loan",
        "make an inference": "draw an inference",
        "in the meanwhile": "in the meantime",
        "lengthy distances": "long distances",
        "maddening crowd": "madding crowd",
        "Magna Charta": "Magna Carta",
        "mariage de convenance": "marriage of convenience",
        "Meantime,": "Meanwhile,",
        "Middle West": "Midwest",
        "Middle Western": "Midwestern",
        "modes of operandi": "modi operandi",
        "mode of operandi": "modus operandi",
        "notion seconded": "motion seconded",
        "mucus membranes": "mucous membranes",
        "must past muster": "must pass muster",
        "neck-in-neck": "neck-and-neck",
        "no-holes-barred": "no-holds-barred",
        "oil magnet": "oil magnate",
        "punch up the lead": "punch up the lede",
        "railroad magnet": "railroad magnate",
        "seconded the notion": "seconded the motion",
        "statute of limits": "statute of limitationas",
        "take prescience over": "take precedence over",
        "both of the last two": "the last two",
        "both of the last": "the last two",
        "inorganic food": "unorganic food",
        "veil of tears": "vale of tears",
        "Venus's flytrap": "Venus flytrap",
        "Venus' flytrap": "Venus flytrap",
        "was accused with": "was accused of",
        # Verbosity
        "make an attempt to": "try to",
        "make attempts to": "try to",
        "make efforts to": "try to",
        "made an attempt to": "tried to",
        "made attempts to": "tried to",
        "made efforts to": "tried to",
        "modern-day": "modern",
        # Grammar
        "be mislead": "be misled",
        "was mislead": "was misled",
        "were mislead": "were misled",
        # Euphemisms
        "armed reconnaissance": "a search-and-destroy mission",
        "pregnancy termination": "abortion",
        "sexually ambidextrous": "bisexual",
        "extermination engineer": "exterminator",
        "permanent layoff": "firing",
        "rodent operative": "rat-catcher",
        # Tenses
        "mistaked": "mistook",
        # Accents
        "ne": "né",
        "nee": "née",
    }

    return preferred_forms_check_opti(text, items, err, msg)


registry.register("misc.preferred_forms.garner", check)
