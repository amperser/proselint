# -*- coding: utf-8 -*-
"""MAU104: Commercialese.

---
layout:     post
error_code: MAU104
source:     Garner's Modern American Usage
source_url: http://amzn.to/15wF76r
title:      commercialese
date:       2014-06-10 12:31:19
categories: writing
---

Archaism.

"""
from proselint.tools import blacklist

err = "MAU104"
msg = u"'{}' is commercialese."

commercialese = [
    "acknowledging yours of",
    "beg to advise",
    "enclosed herewith",
    "enclosed please find",
    "further to yours of",
    "in regard to",
    "inst\.",
    "in the amount of",
    "of even date",
    "pending receipt of",
    "please be advised that",
    "please return same",
    "pleasure of a reply",
    "prox\.",
    "pursuant to your request",
    "regarding the matter",
    "regret to inform",
    "thanking you in advance",
    "the undersigned",
    "this acknowledges your letter",
    "ult\."
    "we are pleased to note",
    "with regard to",
    "your favor has come to hand",
    "yours of even date"
]

check = blacklist(commercialese, err, msg)
