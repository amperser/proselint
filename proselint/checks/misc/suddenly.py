"""
Suddenly.

---
layout:     post
source:     Reference for Writers
source_url: http://bit.ly/1E94vyD
title:      suddenly
date:       2014-06-10 12:31:19
categories: writing
---

“Sudden” means quickly and without warning, but using the word “suddenly” both
slows down the action and warns your reader. Do you know what's more effective
for creating the sense of the sudden? Just saying what happens.

When using “suddenly,” you communicate through the narrator that the action
seemed sudden. By jumping directly into the action, you allow the reader to
experience that suddenness first hand. “Suddenly” also suffers from being
nondescript, failing to communicate the nature of the action itself; providing
no sensory experience or concrete fact to hold on to. Just … suddenly.

Feel free to employ “suddenly” in situations where the suddenness is not
apparent in the action itself. For example, in “Suddenly, I don't hate you
anymore,” the “suddenly” substantially changes the way we think about the
shift in emotional calibration.

"""

from proselint.registry.checks import Check, engine, types

check = Check(
    check_type=types.ExistenceSimple(pattern="Suddenly,"),
    path="misc.suddenly",
    message="Suddenly is nondescript, slows the action, and warns your reader.",
    engine=engine.Fast(opts=engine.RegexOptions(case_insensitive=False)),
)

__register__ = (check,)
