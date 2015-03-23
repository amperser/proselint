# -*- coding: utf-8 -*-
"""MSC: Credit card number printed.

---
layout:     post
error_code: MSC
source:     ???
source_url: ???
title:      credit card number printed
date:       2014-06-10 12:31:19
categories: writing
---

Credit card number printed.

"""
from tools import existence_check, memoize


@memoize
def check(blob):
    """Check the text."""
    err = "MSC102"
    msg = u"Don't put credit card numbers in plain text."

    credit_card_numbers = [
        "4\d{15}",
        "5[1-5]\d{14}",
        "3[4,7]\d{13}",
        "3[0,6,8]\d{12}",
        "6011\d{12}",
    ]

    return existence_check(blob, credit_card_numbers, err, msg)
