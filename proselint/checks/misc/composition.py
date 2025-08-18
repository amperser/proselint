"""
Elementary Principles of Composition.

---
layout:     post
source:     Strunk & White
source_url: ???
title:      Elementary Principles of Composition
date:       2014-06-10 12:31:19
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

from proselint.registry.checks import Check, types

CHECK_PATH = "misc.composition"
CHECK_MESSAGE = "Try '{}' instead of '{}'."

check = Check(
    check_type=types.PreferredFormsSimple(
        items={
            # Put statements in positive form
            "not honest": "dishonest",
            "not important": "unimportant",
            "did not remember": "forgot",
            "did not pay attention to": "ignored",
            "did not have much confidence in": "distrusted",
            # Omit needless words
            "the question as to whether": "whether",
            "there is no doubt but that": "no doubt",
            "used for fuel purposes": "used for fuel",
            "he is a man who": "he",
            "in a hasty manner": "hastily",
            "this is a subject that": "this subject",
            "a strange one": "strange.",
            "the reason why is that": "because",
            "owing to the fact that": "because / since",
            "in spite of the fact that": "although / though",
            "call your attention to the fact that": "remind you / notify you",
            "was unaware of the fact": "did not know / was unaware",
            "did not succeed": "failed",
            "not succeed": "fail",
            "the fact that i had arrived": "my arrival",
        }
    ),
    path=CHECK_PATH,
    message=CHECK_MESSAGE,
)

check_regex = Check(
    check_type=types.PreferredForms(
        items={
            "did not pay (any )?attention to": "ignored",
            "did not have (much )?(confidence|faith) in": "distrusted",
            "(had )?not succeeded": "failed",
        }
    ),
    path=CHECK_PATH,
    message=CHECK_MESSAGE,
)

__register__ = (check, check_regex)
