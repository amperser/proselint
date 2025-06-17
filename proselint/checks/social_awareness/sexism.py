"""
Sexism.

---
layout:     post
source:     Garner's Modern American Usage
source_url: http://bit.ly/1T4alrY
title:      sexism
date:       2014-06-10 12:31:19
categories: writing
---

Points out sexist language.

"""

from proselint.registry.checks import Check, types

CHECK_PATH = "social_awareness.sexism"

check_sexism = Check(
    check_type=types.PreferredFormsSimple(
        items={
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
            # "heroine": "hero"
        }
    ),
    path=CHECK_PATH,
    message="Gender bias. Use '{}' instead of '{}'.",
)

check_preferred = Check(
    check_type=types.PreferredFormsSimple(
        items={
            "anchorperson": "anchor",
            "chairperson": "chair",
            "draftperson": "drafter",
            "ombudsperson": "ombuds",
            "tribesperson": "tribe member",
            "policeperson": "police officer",
            "fireperson": "firefighter",
            "mailperson": "mail carrier",
        }
    ),
    path=CHECK_PATH,
    message="Not a preferred form. Use '{}' instead of '{}'.",
)

__register__ = (check_sexism, check_preferred)
