# -*- coding: utf-8 -*-
u"""Don't start a paragraph with 'But'.

---
layout:
source: Justin Jungé
source_url:
title:
date:       2016-03-10 12:31:19
categories: writing
---

Paragraphs should not start with certain bad words.

"""
from proselint.tools import memoize, existence_check


@memoize
def check(text):
    """Do not start a paragraph with a 'But'."""
    err = "misc.but"
    msg = u"No paragraph should start with a 'But'."
    regex = "(^|([\n\r]+))(\s*)But"
    return existence_check(text, [regex], err, msg)
