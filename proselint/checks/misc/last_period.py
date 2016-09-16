# -*- coding: utf-8 -*-
u"""Check for missing period at end of last sentence in a paragraph

---
layout: 
source: ???
source_url:
title:
date:       2016-09-14 12:31:19
categories: writing
---

Paragraphs should not end with a sentence that does not end with a period.

"""
from proselint.tools import memoize, existence_check


#@memoize #TODO
def check_last_paragraph_period(text):
    """Do not end a paragraph without a period."""
    err = "misc.but"
    msg = u"No paragraph should start with a 'But'."
    regex = "[a-z](^|([\n\r]+))(\s*)"
    return existence_check(text, [regex], err, msg)
