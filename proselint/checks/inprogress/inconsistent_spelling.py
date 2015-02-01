# -*- coding: utf-8 -*-
"""IEL100: Inconsistent spelling.

---
layout:     post
error_code: IEL100
source:     Intelligent Editing Ltd.
source_url: http://bit.ly/1x3hYj7
title:      Inconsistent spelling
date:       2014-06-10 12:31:19
categories: writing
---

Intelligent Editing Ltd. says:

> Some words have more than one correct spelling. American, British, Australian
and Canadian English all have their own preferences. Even within those, there
can be multiple spellings. For example, in the UK 'realise' is often preferred.
However, 'realize' has been used in British-English for centuries and is
preferred in the Oxford English Dictionary. However, no matter which spelling
is preferred, one thing is always wrong: you mustn't use two different
spellings in the same document.
"""

import re


def check(text):

    error_code = "IEL100"
    msg = "Inconsistent spelling of {}."

    inconsistently_spelled_words = [
        ["organis(?:e|ed|ing)", "organiz(?:e|ed|ing)"],
        ["centre", "center"],
        ["focussed", "focused"],
        ["recognise", "recognize"]
    ]

#     errors = []
#     for word_pair in inconsistently_spelled_words:
#         occ = [0, 0]
#         for i in range(2):
#             occ[i] = [m.start() for m in
#                               re.finditer(word_pair[i], text.lower())]

#         if occ[0] > 0 and occ[1] > 0:
#             if occ[0] >= occ[1]:


# errors.append((1, o, error_code, msg.format(word_pair[0] + '/' word_pair[1])))
#     return errors
