"""Em vs. im, en vs. in."""

from __future__ import annotations

from proselint.checks import CheckResult
from proselint.checks import preferred_forms_check_opti

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "We shall imbark on a voyage.",
]


def check(text: str) -> list[CheckResult]:
    """em- vs. en-, im- vs. in-."""
    err = "spelling.em_im_en_in"
    msg = "em-, im-, en-, and in-. '{}' is the preferred spelling."

    items: dict[str, str] = {
        "imbalm": "embalm",
        "imbark": "embark",
        "imbed": "embed",
        "imbitter": "embitter",
        "imblaze": "emblaze",
        "imbody": "embody",
        "imbolden": "embolden",
        "imbosom": "embosom",
        "imbower": "embower",
        "imbrown": "embrown",
        "impanel": "empanel",
        "impower": "empower",
        "incage": "encage",
        "incapsulate": "encapsulate",
        "incase": "encase",
        "inclasp": "enclasp",
        "incumber": "encumber",
        "incumbrance": "encumbrance",
        "indow": "endow",
        "indowment": "endowment",
        "indue": "endue",
        "infold": "enfold",
        "ingraft": "engraft",
        "ingulf": "engulf",
        "inlace": "enlace",
        "inmesh": "enmesh",
        "insheathe": "ensheathe",
        "inshrine": "enshrine",
        "insnare": "ensnare",
        "insoul": "ensoul",
        "insphere": "ensphere",
        "inthrall": "enthrall",
        "inthrone": "enthrone",
        "intitle": "entitle",
        "intomb": "entomb",
        "intreat": "entreat",
        "intrench": "entrench",
        "intrust": "entrust",
        "intwine": "entwine",
        "intwist": "entwist",
        "inwind": "enwind",
        "inwrap": "enwrap",
        "inwreathe": "enwreathe",
        "embrue": "imbrue",
        "empale": "impale",
        "empoverish": "impoverish",
        "enflame": "inflame",
        "engrain": "ingrain",
        "enure": "inure",
    }

    return preferred_forms_check_opti(text, items, err, msg)
