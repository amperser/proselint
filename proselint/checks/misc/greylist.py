"""
Use of greylisted words.

---
layout:     post
source:     Strunk & White
source_url: ???
title:      Use of greylisted words
date:       2014-06-10
categories: writing
---

Strunk & White say:
1. Form the possessive singular of nouns by adding 's.
2. In a series of three or more terms with a conjunction, use a comma after
each term except the last.
3. Enclose parenthetic expressions between commas. ("This rule is difficult to
apply.")
4. Place a comma before a conjunction introducing an independent clause.
5. Do not join independent clauses with a comma; use a semi-colon. Or a period.
6. Do not break sentences in two. Do not use periods for the role of commas.
7. Use a colon after an independent clause if you introduce: a list of
particulars, an appositive, an application, or an illustrative quotation.
8. Use a dash to set off an abrupt break or interruption and to announce a
long appositive or summary.
9. The number of the subject determines the number of the verb. (MDPNB: This
will require nltk & syntactic parsing)
10. Use the proper case(grammatical gender) of pronouns.
    * MDPNB: hard case: "Give this work to whoever looks idle." `whoever looks
    idle` is the object of `to`.
11. A participial phrase at the beginning of a sentence must refer to the
grammatical subject.


"""
from __future__ import annotations

from proselint.checks import CheckResult, existence_check

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "She should utilize her knowledge.",
    "This is obviously an inadvisable word to use obviously.",
    "I utilize a hammer to drive nails into wood.",
    "Do you know anyone who *needs* to utilize the word utilize?",
]


def check(text: str) -> list[CheckResult]:
    """Check the text."""
    err = "misc.greylist.strunk_white"
    msg = "Use of '{}'. {}"

    bad_words = {
        "obviously": "This is obviously an inadvisable word to use.",
        "utilize": "Do you know anyone who needs to utilize the word utilize?",
    }

    results = []
    for word, expl in bad_words.items():
        results.extend(
            existence_check(
                text,
                [word],
                err,
                msg.format(word, expl),
            ),
        )
    return results
