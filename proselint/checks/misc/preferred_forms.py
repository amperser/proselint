"""
Preferred forms.

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

from proselint.registry.checks import Check, Padding, engine, types

CHECK_PATH = "misc.preferred_forms"
CHECK_MESSAGE = "'{}' is the preferred form."

check = Check(
    check_type=types.PreferredFormsSimple(
        padding=Padding.STRICT_WORDS_IN_TEXT,
        items={
            # Obsolete words
            "imprimature": "imprimatur",
            # Proper nouns
            "hallowe'en": "Halloween",
            "haloween": "Halloween",
            "khruschev": "Khrushchev",
            "klu klux klan": "Ku Klux Klan",
            "kruschev": "Khrushchev",
            "pontius pilot": "Pontius Pilate",
            # Plurals
            "hippopotami": "hippopotamuses",
            "longstanding": "long-standing",
            "manifesti": "manifestos",
            "matrixes": "matrices",
            "mongeese": "mongooses",
            "narcissuses": "narcissi",
            "non-sequitur": "non sequitur",
            "retinae": "retinas",
            "sans-serif": "sans serif",
            "sanserif": "sans serif",
            "soprani": "sopranos",
            "titmouses": "titmice",
            "tort feasor": "tortfeasor",
            "tort-feasor": "tortfeasor",
            "trans-ship": "transship",
            "trans-shipped": "transshipped",
            "trans-shipping": "transshipping",
            "tranship": "transship",
            "transhipped": "transshiped",
            "transhipping": "transshipping",
            # Misc
            "mental attitude": "attitude",
            "chief justice of the united states supreme court": (
                "Chief Justice of the United States"
            ),
            "chief justice of the supreme court of the united states": (
                "Chief Justice of the United States"
            ),
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
            "magna charta": "Magna Carta",
            "mariage de convenance": "marriage of convenience",
            "middle west": "Midwest",
            "middle western": "Midwestern",
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
            "venus's flytrap": "Venus flytrap",
            "venus' flytrap": "Venus flytrap",
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
        },
    ),
    path="misc.preferred_forms",
    message="'{}' is the preferred form.",
    engine=engine.Fancy(),
)

# fmt: off
check_meantime_capital = Check(
    check_type=types.PreferredForms(
        items={r"\bMeantime,\B": "Meanwhile,"}, padding=Padding.RAW,
    ),
    path=CHECK_PATH,
    message=CHECK_MESSAGE,
    engine=engine.Fast(opts=engine.RegexOptions(case_insensitive=False)),
)
# fmt: on

check_meantime_clause = Check(
    check_type=types.PreferredForms(
        items={r"\b[;,] meantime,\B": "meanwhile,"}, padding=Padding.RAW
    ),
    path=CHECK_PATH,
    message=CHECK_MESSAGE,
    engine=engine.Fast(opts=engine.RegexOptions(case_insensitive=False)),
    offset=(2, 0),
)

__register__ = (check, check_meantime_capital, check_meantime_clause)
