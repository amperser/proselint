"""Elementary Rules of Usage.

---
layout:     post
source:     Strunk & White
source_url: ???
title:      Elementary Rules of Usage
date:       2014-06-10 12:31:19
categories: writing
---

Strunk & White say:
1. Form the possesive singular of nouns by adding 's.
2. In a series of three or more terms with a conjunction, use a comma after
each term except the last.
3. Enclose parenthetic expressions between commas. ("This rule is difficult to
apply.")
4. Place a comma before a conjunction introducing an independent clause.
5. Do not join independent clauses with a comma; use a semi-colon. Or a period.
6. Do not break sentences in two. Do not use periods for the role of commas.
7. Use a colon after an independent clause if you introduce: a list of
particulars, an appositive, an application, or an illustative quotation.
8. Use a dash to set off an aburpt break or interruption and to announce a
long appositive or summary.
9. The number of the subject determines the number of the verb. (MDPNB: This
will require nltk & syntactic parsing)
10. Use the proper case(grammatical gender) of pronouns.
    * MDPNB: hard case: "Give this work to whoever looks idle." `whoever looks
    idle` is the object of `to`.
11. A participial phrase at the beginning of a sentence must refer to the
grammatical subject.
"""

# from tools import memoize
# import re


# @memoize
# def check(text):
#     err = "strunk_white.usage"
#     msg = "Use of '{}'. {}"

#     bad_words = [
#         "obviously",
#         "utilize"
#     ]

#     explanations = {
#         "obviously":
#         "This is obviously an inadvisable word to use.",
#         "utilize":
#         r"Do you know anyone who *needs* to utilize the word utilize?"
#     }

#     errors = []
#     for word in bad_words:
#         occ = [m for m in re.finditer(word, text.lower())]
#         for o in occ:
#             errors.append((o.start(), o.end(), err,
#                           msg.format(word, explanations[word])))

#     return errors
