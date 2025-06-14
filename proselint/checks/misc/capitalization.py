"""
Incorrect capitalization.

---
layout:     post
source:     Garner's Modern American Usage
source_url: http://bit.ly/1T4alrY
title:      incorrect captalization
date:       2014-06-10 12:31:19
categories: writing
---

Incorrect capitalization.

"""
from proselint.tools import preferred_forms_check


def check(text):
    """Suggest the preferred forms."""
    err = "misc.capitalization.preferred"
    msg = "Incorrect capitalization. '{}' is the preferred form."

    list = [
        ["Stone Age", ["stone age"]],
        ["space age", ["Space Age"]],
        ["the American West", ["the American west"]],
        ["Mother Nature", ["mother nature"]],
    ]

    return preferred_forms_check(text, list, err, msg, ignore_case=False)


#
# def check_seasons(text):
#     """Suggest the preferred forms."""
#     err = "misc.capitalization.seasons"
#     msg = "Seasons shouldn't be capitalized. '{}' is the preferred form."

#     list = [
#         # ["winter",        ["Winter"]],
#         # ["fall",          ["Fall"]],
#         # ["summer",        ["Summer"]],
#         # ["spring",        ["Spring"]],
#     ]

#     return preferred_forms_check(text, list, err, msg, ignore_case=False)


def check_months(text):
    """Suggest the preferred forms."""
    err = "misc.capitalization.months"
    msg = "Months should be capitalized. '{}' is the preferred form."

    list = [
        ["January", ["january"]],
        ["February", ["february"]],
        # ["March",           ["march"]],
        ["April", ["april"]],
        # ["May",             ["may"]],
        ["June", ["june"]],
        ["July", ["july"]],
        ["August", ["august"]],
        ["September", ["september"]],
        ["October", ["october"]],
        ["November", ["november"]],
        ["December", ["december"]],
    ]

    return preferred_forms_check(text, list, err, msg, ignore_case=False)


def check_days(text):
    """Suggest the preferred forms."""
    err = "misc.capitalization.days"
    msg = "Days of the week should be capitalized. '{}' is the preferred form."

    list = [

        ["Monday", ["monday"]],
        ["Tuesday", ["tuesday"]],
        ["Wednesday", ["wednesday"]],
        ["Thursday", ["thursday"]],
        ["Friday", ["friday"]],
        ["Saturday", ["saturday"]],
        ["Sunday", ["sunday"]],
    ]

    return preferred_forms_check(text, list, err, msg, ignore_case=False)
