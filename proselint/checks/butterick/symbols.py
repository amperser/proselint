# -*- coding: utf-8 -*-
"""BTR100: Use the symbols.

---
layout:     post
error_code: BTR100
source:     Butterick's Practical Typography
source_url: http://practicaltypography.com/
title:      Tense present
date:       2014-06-10 12:31:19
categories: writing
---

Use the symbols.

"""
from proselint.tools import memoize
import re


@memoize
def check(text):

    err = "BTR100"

    symbols = [
        ["\s\(c\)\s",    u"'{}' is a goofy alphabetic approximation. Use ©."],
        ["\s\(TM\)\s",   u"'{}' is a goofy alphabetic approximation. Use ™."],
        ["\s\(R\)\s",    u"'{}' is a goofy alphabetic approximation. Use ®."],
        [u"Copy­right ©", u"'{}' is redundant. Use the word or the symbol."],
        [r"\.\.\.",      u"'...' is an approximation, use the ellipsis symbol '…'."],
        [u"[A-Z][a-z]{1,10}[-\u2014][A-Z][a-z]{1,10}", u"Use an en dash (–) to separate names."],
    ]

    errors = []
    for i in symbols:
        for m in re.finditer(i[0], text, flags=re.UNICODE | re.IGNORECASE):
            txt = m.group(0).strip()
            errors.append((m.start(), m.end(), err, i[1].format(txt)))

    return errors
