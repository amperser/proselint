"""
Needless variants.

---
layout:     post
source:     Garner's Modern American Usage
source_url: http://bit.ly/1T4alrY
title:      needless variants
date:       2014-06-10
categories: writing
---

Points out use of needless variants.

"""
from __future__ import annotations

from proselint.checks import CheckResult, preferred_forms_check_opti

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "It was an extensible telescope.",
]


def check_1(text: str) -> list[CheckResult]:
    """
    Suggest the preferred forms.

    NOTE: this was one of the slowest Checks,
          so it was segmented to even the load for parallelization
    """
    err = "needless_variants.misc"
    msg = "'{1}' is a needless variant. '{0}' is the preferred form."

    items: dict[str, str] = {
        "abolishment": "abolition",
        "accessary": "accessory",
        "accreditate": "accredit",
        "accruement": "accrual",
        "accusee": "accused",
        "acquaintanceship": "acquaintance",
        "acquitment": "acquittal",
        "administrate": "administer",
        "administrated": "administered",
        "administrating": "administering",
        "adulterate": "adulterous",
        "advisatory": "advisory",
        "advocator": "advocate",
        "aggrievance": "grievance",
        "allegator": "alleger",
        "allusory": "allusive",
        "amative": "amorous",
        "amortizement": "amortization",
        "amphiboly": "amphibology",
        "anecdotalist": "anecdotist",
        "anilinctus": "anilingus",
        "anticipative": "anticipatory",
        "antithetic": "antithetical",
        "applicative": "applicable",
        "applicatory": "applicable",
        "applier": "applicator",
        "approbative": "approbatory",
        "arbitrager": "arbitrageur",
        "arsenous": "arsenious",
        "ascendance": "ascendancy",
        "ascendence": "ascendancy",
        "ascendency": "ascendancy",
        "auctorial": "authorial",
        "averral": "averment",
        "barbwire": "barbed wire",
        "benefic": "beneficent",
        "benignant": "benign",
        "bestowment": "bestowal",
        "betrothment": "betrothal",
        "blamableness": "blameworthiness",
        "butt naked": "buck naked",
        "camarade": "comrade",
        "capturer": "captor",
        "carta blanca": "carte blanche",
        "casualities": "casualties",
        "casuality": "casualty",
        "catch on fire": "catch fire",
        "catholicly": "catholically",
        "cease fire": "ceasefire",
        "cell phone": "cellphone",
        "cell-phone": "cellphone",
        "channelize": "channel",
        "chaplainship": "chaplaincy",
        "chrysalid": "chrysalis",
        "chrysalids": "chrysalises",
        "cigaret": "cigarette",
        "cliquey": "cliquish",
        "cliquy": "cliquish",
        "coemployee": "coworker",
        "cognitional": "cognitive",
        "cohabitate": "cohabit",
        "cohabitor": "cohabitant",
        "collodium": "collodion",
        "collusory": "collusive",
        "commemoratory": "commemorative",
        "commonty": "commonage",
        "communicatory": "communicative",
        "compensative": "compensatory",
        "complacence": "complacency",
        "complicitous": "complicit",
        "computate": "compute",
        "conciliative": "conciliatory",
        "concomitancy": "concomitance",
        "condonance": "condonation",
        "confirmative": "confirmatory",
        "congruency": "congruence",
        "connotate": "connote",
        "consanguineal": "consanguine",
        "conspicuity": "conspicuousness",
        "conspiratorialist": "conspirator",
        "constitutionist": "constitutionalist",
        "contingence": "contigency",
        "contributary": "contributory",
        "contumacity": "contumacy",
        "conversible": "convertible",
        "conveyal": "conveyance",
        "corroboratory": "corroborative",
        "cotemporaneous": "contemporaneous",
        "cotemporary": "contemporary",
        "cumbrance": "encumbrance",
        "cumulate": "accumulate",
        "curatory": "curative",
        "daredeviltry": "daredevilry",
        "deceptious": "deceptive",
        "defamative": "defamatory",
        "defraudulent": "fraudulent",
        "degeneratory": "degenerative",
        "delimitate": "delimit",
        "delusory": "delusive",
        "denouncement": "denunciation",
        "depositee": "depositary",
        "depreciative": "depreciatory",
        "deprival": "deprivation",
        "derogative": "derogatory",
        "destroyable": "destructible",
        "detoxicate": "detoxify",
        "detractory": "detractive",
        "deviancy": "deviance",
        "deviationist": "deviant",
        "digamy": "deuterogamy",
        "digitalize": "digitize",
        "diminishment": "diminution",
        "diplomatist": "diplomat",
        "disassociate": "dissociate",
        "disciplinatory": "disciplinary",
        "discriminant": "discriminating",
        "disenthrone": "dethrone",
        "disintegratory": "disintegrative",
        "dismission": "dismissal",
        "disorientate": "disorient",
        "disorientated": "disoriented",
        "disquieten": "disquiet",
        "distraite": "distrait",
        "divergency": "divergence",
        "dividable": "divisible",
        "doctrinary": "doctrinaire",
        "documental": "documentary",
        "domesticize": "domesticate",
        "duplicatory": "duplicative",
        "duteous": "dutiful",
        "educationalist": "educationist",
        "educatory": "educative",
        "enigmatas": "enigmas",
        "enlargen": "enlarge",
        "epical": "epic",
        "erotism": "eroticism",
        "ethician": "ethicist",
        "ex officiis": "ex officio",
        "exculpative": "exculpatory",
        "exigeant": "exigent",
        "exigence": "exigency",
        "exotism": "exoticism",
        "expedience": "expediency",
        "expediential": "expedient",
        "extensible": "extendable",
        "eying": "eyeing",
        "fiefdom": "fief",
        "flagrance": "flagrancy",
        "flatulency": "flatulence",
        "fraudful": "fraudulent",
        "funebrial": "funereal",
        "geographical": "geographic",
        "geometrical": "geometric",
        "goatherder": "goatherd",
        "gustatorial": "gustatory",
        "habitude": "habit",
        "henceforward": "henceforth",
        "hesitance": "hesitancy",
        "heterogenous": "heterogeneous",
        "hierarchic": "hierarchical",
        "hindermost": "hindmost",
        "honorand": "honoree",
        "hypostasize": "hypostatize",
        "hysteric": "hysterical",
        "impanel": "empanel",
        "indow": "endow",
        "indue": "endue",
        "meliorate": "ameliorate",
        "misdoubt": "doubt",
        "parachronism": "anachronism",
    }

    return preferred_forms_check_opti(text, items, err, msg)


def check_2(text: str) -> list[CheckResult]:
    """
    Suggest the preferred forms.

    NOTE: this was one of the slowest Checks,
          so it was segmented to even the load for parallelization
    """
    err = "needless_variants.misc"
    msg = "'{1}' is a needless variant. '{0}' is the preferred form."

    items: dict[str, str] = {
        "Coffee klatsch": "kaffeeklatsch",
        "Zoroastrism": "Zoroastrianism",
        "coffee klatch": "kaffeeklatsch",
        "copartner": "partner",
        "copartnership": "partnership",
        "criminate": "incriminate",
        "culpatory": "inculpatory",
        "enswathe": "swathe",
        "gerry-rigged": "jury-rigged",
        "idolatrize": "idolize",
        "imperviable": "impervious",
        "importunacy": "importunity",
        "impotency": "impotence",
        "imprimatura": "imprimatur",
        "improprietous": "improper",
        "inalterable": "unalterable",
        "incitation": "incitement",
        "incommunicative": "uncommunicative",
        "inconsistence": "inconsistency",
        "incontrollable": "uncontrollable",
        "incurment": "incurrence",
        "inhibitive": "inhibitory",
        "innavigable": "unnavigable",
        "innovational": "innovative",
        "inquisitional": "inquisitorial",
        "insistment": "insistence",
        "insolvable": "unsolvable",
        "instillment": "instillation",
        "instinctual": "instinctive",
        "insuror": "insurer",
        "insurrectional": "insurrectionary",
        "interpretate": "interpret",
        "intervenience": "intervention",
        "ironical": "ironic",
        "jerry-rigged": "jury-rigged",
        "judgmatic": "judgmental",
        "labyrinthian": "labyrinthine",
        "laudative": "laudatory",
        "legitimatization": "legitimation",
        "legitimatize": "legitimize",
        "legitimization": "legitimation",
        "lengthways": "lengthwise",
        "life-sized": "life-size",
        "liquorice": "licorice",
        "lithesome": "lithe",
        "lollipop": "lollypop",
        "loth": "loath",
        "lubricous": "lubricious",
        "maihem": "mayhem",
        "medicinal marijuana": "medical marijuana",
        "minimalize": "minimize",
        "mirk": "murk",
        "mirky": "murky",
        "monetarize": "monetize",
        "moveable": "movable",
        "narcism": "narcissism",
        "neglective": "neglectful",
        "negligency": "negligence",
        "neologizer": "neologist",
        "neurologic": "neurological",
        "nicknack": "knickknack",
        "nictate": "nictitate",
        "nonenforceable": "unenforceable",
        "normalcy": "normality",
        "numbedness": "numbness",
        "omittable": "omissible",
        "onomatopoetic": "onomatopoeic",
        "opinioned": "opined",
        "optimum advantage": "optimal advantage",
        "orientate": "orient",
        "outsized": "outsize",
        "oversized": "oversize",
        "overthrowal": "overthrow",
        "pacificist": "pacifist",
        "paederast": "pederast",
        "parti-color": "parti-colored",
        "participative": "participatory",
        "party-colored": "parti-colored",
        # "passcode": "password",  # common term > 2020
        "patine": "patina",
        "pediatrist": "pediatrician",
        "penumbrous": "penumbral",
        "perjorative": "pejorative",
        "permissory": "permissive",
        "permutate": "permute",
        "personation": "impersonation",
        "pharmaceutic": "pharmaceutical",
        "pleuritis": "pleurisy",
        "policy holder": "policyholder",
        "policyowner": "policyholder",
        "politicalize": "politicize",
        "precedency": "precedence",
        "preceptoral": "preceptorial",
        "precipitance": "precipitancy",
        "precipitant": "precipitate",
        "preclusory": "preclusive",
        "precolumbian": "pre-Columbian",
        "prefectoral": "prefectorial",
        "preponderately": "preponderantly",
        "preserval": "preservation",
        "preventative": "preventive",
        "proconsulship": "proconsulate",
        "procreational": "procreative",
        "procurance": "procurement",
        "propelment": "propulsion",
        "propulsory": "propulsive",
        "prosecutive": "prosecutory",
        "protectory": "protective",
        "provocatory": "provocative",
        "pruriency": "prurience",
        "psychal": "psychical",
        "punitory": "punitive",
        "pygmaen": "pygmy",
        "pygmean": "pygmy",
        "quantitate": "quantify",
        "questionary": "questionnaire",
        "quiescency": "quiescence",
        "rabbin": "rabbi",
        "reasonability": "reasonableness",
        "recidivistic": "recidivous",
        "recriminative": "recriminatory",
        "recruital": "recruitment",
        "recurrency": "recurrence",
        "recusance": "recusancy",
        "recusation": "recusal",
        "recusement": "recusal",
        "redemptory": "redemptive",
        "referrable": "referable",
        "referrible": "referable",
        "refutatory": "refutative",
        "remitment": "remittance",
        "remittal": "remission",
        "renouncement": "renunciation",
        "renunciable": "renounceable",
        "reparatory": "reparative",
        "repudiative": "repudiatory",
        "requitement": "requital",
        "rescindment": "rescission",
        "restoral": "restoration",
        "reticency": "reticence",
        "retributional": "retributive",
        "retributionary": "retributive",
        "reviewal": "review",
        "revisal": "revision",
        "revisional": "revisionary",
        "revokable": "revocable",
        "revokeable": "revocable",
        "revolute": "revolt",
        "saliency": "salience",
        "salutiferous": "salutary",
        "sensatory": "sensory",
        "sessionary": "sessional",
        "shareowner": "shareholder",
        "sicklily": "sickly",
        "signator": "signatory",
        "slanderize": "slander",
        "societary": "societal",
        "sodomist": "sodomite",
        "solicitate": "solicit",
        "speculatory": "speculative",
        "spiritous": "spirituous",
        "statutorial": "statutory",
        "submergeable": "submersible",
        "submittal": "submission",
        "subtile": "subtle",
        "succuba": "succubus",
        "sufficience": "sufficiency",
        "suppliant": "supplicant",
        "surmisal": "surmise",
        "suspendible": "suspendable",
        "synthetize": "synthesize",
        "systemize": "systematize",
        "tactual": "tactile",
        "tangental": "tangential",
        "tautologous": "tautological",
        "tee-shirt": "T-shirt",
        "thenceforward": "thenceforth",
        "transiency": "transience",
        "transposal": "transposition",
        "unfrequent": "infrequent",
        "unreasonability": "unreasonableness",
        "unrevokable": "irrevocable",
        "unsubstantial": "insubstantial",
        "usurpature": "usurpation",
        "variative": "variational",
        "vegetive": "vegetative",
        "vindicative": "vindictive",
        "vituperous": "vituperative",
        "vociferant": "vociferous",
        "volitive": "volitional",
        "wolverene": "wolverine",
        "wolvish": "wolfish",
    }

    return preferred_forms_check_opti(text, items, err, msg)
