"""WGD200: Lexical illusions.

---
layout:     post
error_code: WGD200
source:     write-good
source_url: https://github.com/btford/write-good
title:      WGD200&#58; Lexical illusion present
date:       2014-06-10 12:31:19
categories: writing
---

A lexical illusion happens when a word word is unintentiall repeated twice, and
and this happens most often between line breaks.

"""


def check(text):

    error_code = "WGD200"
    msg = "Lexical illusion present."

    return [(1, 1, error_code, msg)]
