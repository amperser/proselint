"""
Sexism.

---
layout:     post
source:     Garner's Modern American Usage
source_url: http://bit.ly/1T4alrY
title:      sexism
date:       2014-06-10
categories: writing
---

Points out sexist language.

"""
from __future__ import annotations

from proselint.checks import CheckResult, preferred_forms_check_opti

examples_pass = [
    "Smoke phrase with nothing flagged.",
    "Hello Mr. Birdperson. You look good.",
    "Hello Mr. birdperson. still looking good.",
    "Oh Chairperson - happy face.",
]

examples_fail = [
    "The legal team had two lawyers and a lady lawyer.",
    "Oh chairperson - why so sad.",
    "You get the mailperson.",
]


def check_sexism(text: str) -> list[CheckResult]:
    """Suggest the preferred forms."""
    err = "sexism.misc"
    msg = "Gender bias. Use '{}' instead of '{}'."

    # TODO: actress, postman
    items: dict[str, str] = {
        "anchorman": "anchor",
        "anchorwoman": "anchor",
        "chairman": "chair",
        "chairwoman": "chair",
        "draftman": "drafter",
        "draftwoman": "drafter",
        "ombudsman": "ombuds",
        "ombudswoman": "ombuds",
        "tribesman": "tribe member",
        "tribeswoman": "tribe member",
        "policeman": "police officer",
        "policewoman": "police officer",
        "fireman": "firefighter",
        "firewoman": "firefighter",
        "mailman": "mail carrier",
        "mailwoman": "mail carrier",
        "herstory": "history",
        "womyn": "women",
        "poetess": "poet",
        "authoress": "author",
        "waitress": "waiter",
        "lady lawyer": "lawyer",
        "woman doctor": "doctor",
        "female booksalesman": "bookseller",
        "female airman": "air pilot",
        "executrix": "executor",
        "prosecutrix": "prosecutor",
        "testatrix": "testator",
        "man and wife": "husband and wife",
        "chairmen and chairs": "chairs",
        "men and girls": "men and women",
        "comedienne": "comedian",
        "confidante": "confidant",
        "woman scientist": "scientist",
        "women scientists": "scientists",
        # "heroine": "hero",
    }

    return preferred_forms_check_opti(text, items, err, msg, ignore_case=False)


def check_preferred_form(text: str) -> list[CheckResult]:
    """Suggest the preferred forms."""
    err = "sexism.misc"
    msg = "Not a preferred form. Use '{}' instead of '{}'."

    items: dict[str, str] = {
        "anchorperson": "anchor",
        "chairperson": "chair",
        "draftperson": "drafter",
        "ombudsperson": "ombuds",
        "tribesperson": "tribe member",
        "policeperson": "police officer",
        "fireperson": "firefighter",
        "mailperson": "mail carrier",
    }
    return preferred_forms_check_opti(text, items, err, msg, ignore_case=False)
