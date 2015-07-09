"""Elementary Rules of Usage.

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
4.1. Placing negative and positive in oposition makes for a stronger structure.
    * Ex. Not charity, but simple justice.
    * Not that I loved Caesar less, but that I loved Rome more.
4.2. Do not use unnecessary auxillaries or conditionals.
5. Use definite, specific, concrete language.
    * A period of unfavorable weather set in. ->It rained every day for a week.
6. Omit needless words.
    * `The fact that` is particularly pernicious.
    * `who is, which was` and the like are often superfluous
7. Avoid a succession of loose sentences.
    * MDPNB Principle of brevity. Take 2.
8. Express coordinate ideas in similar form.
    * MDPNB: Prinicple of parrallel structure.
    * MDPNB: This one will be hard...
9. Keep related words together.
    * MDPNB: Principle of localism in semantics.
10. In summaries, keep to one tense.
    * MDPNB: Principle of temporal consistency.
11. Place the emphatic word of a sentence at the end.
    * MDPNB: Principle of recency.
"""
from tools import memoize, preferred_forms_check


@memoize
def check(text):
    """Suggest the preferred forms."""
    err = "strunk_white.composition"
    msg = "Try '{}' instead of '{}'."

    bad_forms = [
        # Put statements in positive form
        ["dishonest",               ["not honest"]],
        ["trifling",                ["not important"]],
        ["forgot",                  ["did not remember"]],
        ["ignored",                 ["did not pay (any )?attention to"]],
        ["distrusted",              ["did not have much confidence in"]],

        # Omit needless words
        ["whether",                 ["the question as to whether"]],
        ["no doubt",                ["there is no doubt but that"]],
        ["used for fuel",           ["used for fuel purposes"]],
        ["he",                      ["he is a man who"]],
        ["hastily",                 ["in a hasty manner"]],
        ["this subject",            ["this is a subject that"]],
        ["Her story is strange.",   ["Her story is a strange one."]],
        ["because",                 ["the reason why is that"]],
        ["because / since",         ["owing to the fact that"]],
        ["although / though",       ["in spite of the fact that"]],
        ["remind you / notify you",
            ["call your attention to the fact that"]],
        ["I did not know that / I was unaware that",
            ["I was unaware of the fact that"]],
        ["his failure",             ["the fact that he had not succeeded"]],
        ["my arrival",              ["the fact that i had arrived"]]
    ]

    return preferred_forms_check(text, bad_forms, err, msg)
