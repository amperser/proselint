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

from proselint.checks import CheckRegistry, CheckSpec, PreferredFormsSimple

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

check_sexism = CheckSpec(
    # TODO: actress, postman
    # note for the former that a similar issue to heroine exists, and for the
    # latter, advice conflicting with other entries exists (i.e. postperson)
    PreferredFormsSimple({
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
    }),
    "sexism.misc",
    "Gender bias. Use '{}' instead of '{}'.",
    ignore_case=False,
)

check_preferred_form = CheckSpec(
    PreferredFormsSimple({
        "anchorperson": "anchor",
        "chairperson": "chair",
        "draftperson": "drafter",
        "ombudsperson": "ombuds",
        "tribesperson": "tribe member",
        "policeperson": "police officer",
        "fireperson": "firefighter",
        "mailperson": "mail carrier",
    }),
    "sexism.misc",
    "Not a preferred form. Use '{}' instead of '{}'.",
)


def register_with(registry: CheckRegistry) -> None:
    """Register the checks."""
    registry.register_many((
        check_sexism,
        check_preferred_form,
    ))
