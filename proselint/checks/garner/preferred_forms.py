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
def check(blob):
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
        ["sans serif",          ["sans-serif", "sanserif"]],
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
        ["mortgagor",           ["mortgager"]],
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
        ["mustache",            ["moustache"]],
        ["friend in common",    ["mutual friend"]],
        ["not nearly as",       ["nowhere near as"]],
        ["off",                 ["off of"]],
        ["knowing that",        ["in light of the fact that"]],
        ["lanyard",             ["laniard"]],
        ["largess",             ["largesse"]],
        ["lasagna",             ["lasagne"]],
        ["Chief Justice of the United States",
            ["Chief Justice of the United States Supreme Court",
             "Chief Justice of the Supreme Court of the United States."]],
        ["podiatry",            ["chiropody"]],
        ["podiatrist",          ["chiropodist"]],
        ["chitterlings",        ["chitlings", "chitlins"]],
        ["combustion engine",   ["combustible engine"]],

        # Idioms
        ["madding crowd",       ["maddening crowd"]],
        ["come off it",         ["come off of it"]],
        ["was accused of"],     ["was accused with"],
        ["all the time",        ["all of the time"]],
        ["as follows",          ["as follow"]],
        ["the last two",        ["both of the last two"]],
        ["the last two",        ["both of the last"]],
        ["bulk large",          ["bulk largely"]],
        ["a couple of people",  ["a couple people"]],
        ["dear departed",       ["dearly departed"]],
        ["default on a loan",   ["default to a loan"]],

        # TODO, entries that are a bit complicated
        # announce
    ]

    return preferred_forms_check(blob, preferences, err, msg)


@memoize
def check_able_ible(blob):
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

    return preferred_forms_check(blob, preferences, err, msg)


@memoize
def check_able_atable(blob):
    """-able vs. -ible."""
    err = "MAU102"
    msg = "-able vs. -atable. '{}' is the preferred form."

    preferences = [

        ["abbreviable",       ["abbreviatable"]],
        ["abdicable",         ["abdicatable"]],
        ["abrogable",         ["abrogatable"]],
        ["accommodable",      ["accommodatable"]],
        ["accumulable",       ["accumulatable"]],
        ["activable",         ["activatable"]],
        ["administrable",     ["administratable"]],
        ["adulterable",       ["adulteratable"]],
        ["affiliable",        ["affiliatable"]],
        ["aggregable",        ["aggregatable"]],
        ["agitable",          ["agitatable"]],
        ["alienable",         ["alienatable"]],
        ["alleviable",        ["alleviatable"]],
        ["allocable",         ["allocatable"]],
        ["ameliorable",       ["amelioratable"]],
        ["annihilable",       ["annihilatable"]],
        ["appreciable",       ["appreciatable"]],
        ["appropriable",      ["appropriatable"]],
        ["arbitrable",        ["arbitratable"]],
        ["articulable",       ["articulatable"]],
        ["calculable",        ["calculatable"]],
        ["communicable",      ["communicatable"]],
        ["compensable",       ["compensatable"]],
        ["confiscable",       ["confiscatable"]],
        ["corroborable",      ["corroboratable"]],
        ["cultivable",        ["cultivatable"]],
        ["delegable",         ["delegatable"]],
        ["delineable",        ["delineatable"]],
        ["demonstrable",      ["demonstratable"]],
        ["detonable",         ["detonatable"]],
        ["differentiable",    ["differentiatable"]],
        ["eradicable",        ["eradicatable"]],
        ["evacuable",         ["evacuatable"]],
        ["evaluable",         ["evaluatable"]],
        ["expropriable",      ["expropriatable"]],
        ["generable",         ["generatable"]],
        ["indicable",         ["indicatable"]],
        ["inebriable",        ["inebriatable"]],
        ["inextirpable",      ["inextirpatable"]],
        ["inextricable",      ["inextricatable"]],
        ["infatuable",        ["infatuatable"]],
        ["infuriable",        ["infuriatable"]],
        ["invalidable",       ["invalidatable"]],
        ["investigable",      ["investigatable"]],
        ["isolable",          ["isolatable"]],
        ["litigable",         ["litigatable"]],
        ["manipulable",       ["manipulatable"]],
        ["medicable",         ["medicatable"]],
        ["navigable",         ["navigatable"]],
        ["obligable",         ["obligatable"]],
        ["obviable",          ["obviatable"]],
        ["operable",          ["operatable"]],
        ["originable",        ["originatable"]],
        ["participable",      ["participatable"]],
        ["penetrable",        ["penetratable"]],
        ["perpetrable",       ["perpetratable"]],
        ["perpetuable",       ["perpetuatable"]],
        ["predicable",        ["predicatable"]],
        ["propagable",        ["propagatable"]],
        ["regulable",         ["regulatable"]],
        ["replicable",        ["replicatable"]],
        ["repudiable",        ["repudiatable"]],
        ["segregable",        ["segregatable"]],
        ["separable",         ["separatable"]],
        ["subjugable",        ["subjugatable"]],
        ["vindicable",        ["vindicatable"]],
        ["violable",          ["violatable"]],
        ["vitiable",          ["vitiatable"]]
    ]

    return preferred_forms_check(blob, preferences, err, msg)


@memoize
def check_em_vs_em_and_en_vs_in(blob):
    """em- vs. en-, im- vs. in-."""
    err = "MAU102"
    msg = "'{}' is the preferred form."

    preferences = [

        ["embalm",      ["imbalm"]],
        ["embark",      ["imbark"]],
        ["embed",       ["imbed"]],
        ["embitter",    ["imbitter"]],
        ["emblaze",     ["imblaze"]],
        ["embody",      ["imbody"]],
        ["embolden",    ["imbolden"]],
        ["embosom",     ["imbosom"]],
        ["embower",     ["imbower"]],
        ["embrown",     ["imbrown"]],
        ["empanel",     ["impanel"]],
        ["empower",     ["impower"]],
        ["encage",      ["incage"]],
        ["encapsulate", ["incapsulate"]],
        ["encase",      ["incase"]],
        ["enclasp",     ["inclasp"]],
        ["encumber",    ["incumber"]],
        ["encumbrance", ["incumbrance"]],
        ["endow",       ["indow"]],
        ["endowment",   ["indowment"]],
        ["endue",       ["indue"]],
        ["enfold",      ["infold"]],
        ["engraft",     ["ingraft"]],
        ["engulf",      ["ingulf"]],
        ["enlace",      ["inlace"]],
        ["enmesh",      ["inmesh"]],
        ["ensheathe",   ["insheathe"]],
        ["enshrine",    ["inshrine"]],
        ["ensnare",     ["insnare"]],
        ["ensoul",      ["insoul"]],
        ["ensphere",    ["insphere"]],
        ["enthrall",    ["inthrall"]],
        ["enthrone",    ["inthrone"]],
        ["entitle",     ["intitle"]],
        ["entomb",      ["intomb"]],
        ["entreat",     ["intreat"]],
        ["entrench",    ["intrench"]],
        ["entrust",     ["intrust"]],
        ["entwine",     ["intwine"]],
        ["entwist",     ["intwist"]],
        ["enwind",      ["inwind"]],
        ["enwrap",      ["inwrap"]],
        ["enwreathe",   ["inwreathe"]],
        ["imbrue",      ["embrue"]],
        ["impale",      ["empale"]],
        ["impoverish",  ["empoverish"]],
        ["inflame",     ["enflame"]],
        ["ingrain",     ["engrain"]],
        ["inure",       ["enure"]],
    ]

    return preferred_forms_check(blob, preferences, err, msg)
