"""Elementary Rules of Usage.

---
layout:     post
source:     Strunk & White
source_url: ???
title:      Elementary Principles of Composition
date:       2014-06-10
categories: writing
---

Strunk & White say:
1. Choose a suitable design and hold to it.
    * MDPNB: Sounds like a principle of `consistency`.
2. Make the paragraph the unit of composition.
    * MDPNB: This can be generalized to say something about variability in the
    length of paragraphs and sentences. When any device is too often used it
    becomes a mannerism.
    * MDPNB: Sounds like a principle of `variation`.
3. Use the active voice.
4. Put statements in positive form.
    * MDPNB: In some cases this will apply as an invective against the use of
    a double negative.
    * Ex: He was not very often on time. -> He usually came late.
    * Ex:
4.1. Placing negative and positive in opposition makes for a stronger
structure.
    * Ex. Not charity, but simple justice.
    * Not that I loved Caesar less, but that I loved Rome more.
4.2. Do not use unnecessary auxiliaries or conditionals.
5. Use definite, specific, concrete language.
    * A period of unfavorable weather set in. ->It rained every day for a week.
6. Omit needless words.
    * `The fact that` is particularly pernicious.
    * `who is, which was` and the like are often superfluous
7. Avoid a succession of loose sentences.
    * MDPNB Principle of brevity. Take 2.
8. Express coordinate ideas in similar form.
    * MDPNB: Principle of parallel structure.
    * MDPNB: This one will be hard...
9. Keep related words together.
    * MDPNB: Principle of localism in semantics.
10. In summaries, keep to one tense.
    * MDPNB: Principle of temporal consistency.
11. Place the emphatic word of a sentence at the end.
    * MDPNB: Principle of recency.
"""
from __future__ import annotations

from proselint.checks import CheckResult
from proselint.checks import preferred_forms_check_opti
from proselint.checks import preferred_forms_check_regex

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "His story is not honest.",
    "Her story is a strange one.",
    "He had not succeeded.",
    "He had not succeeded with that.",
]


def check(text: str) -> list[CheckResult]:
    """Suggest the preferred forms."""
    err = "misc.composition.strunk_white"
    msg = "Try '{}' instead of '{}'."

    items: dict[str, str] = {
        # Put statements in positive form
        "not honest": "dishonest",
        "not important": "unimportant",
        "did not remember": "forgot",
        "did not have much confidence in": "distrusted",
        # Omit needless words
        "the question as to whether": "whether",
        "there is no doubt but that": "no doubt",
        "used for fuel purposes": "used for fuel",
        "he is a man who": "he",
        "in a hasty manner": "hastily",
        "this is a subject that": "this subject",
        "a strange one": "strange",
        "the reason why is that": "because",
        "owing to the fact that": "because / since",
        "in spite of the fact that": "although / though",
        "call your attention to the fact that": "remind you / notify you",
        "I was unaware of the fact that": "I did not know that / I was unaware that",
        "not succeed": "fail",
        "the fact that i had arrived": "my arrival",
    }
    ret1 = preferred_forms_check_opti(text, items, err, msg)

    items_regex: dict[str, str] = {
        r"did not pay (any )?attention to": "ignored",
        r"(had )?not succeeded": "failed",
    }
    ret2 = preferred_forms_check_regex(text, items_regex, err, msg)

    return ret1 + ret2
