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
from proselint.tools import memoize, existence_check


@memoize
def check_ellipsis(blob):
    """Use an ellipsis instead of three dots."""
    err = "BTR101"
    msg = u"'...' is an approximation, use the ellipsis symbol '…'."
    regex = "\.\.\."

    return existence_check(blob, [regex], err, msg, max_errors=3,
                           require_padding=False, offset=0)


@memoize
def check_copyright_symbol(blob):
    """Use the copyright symbol instead of (c)."""
    err = "BTR102"
    msg = u"(c) is a goofy alphabetic approximation, use the symbol ©."
    regex = "\([cC]\)"

    return existence_check(
        blob, [regex], err, msg, max_errors=1, require_padding=False)


@memoize
def check_trademark_symbol(blob):
    """Use the trademark symbol instead of (c)."""
    err = "BTR103"
    msg = u"(TM) is a goofy alphabetic approximation, use the symbol ™."
    regex = "\(TM\)"

    return existence_check(
        blob, [regex], err, msg, max_errors=3, require_padding=False)


@memoize
def check_registered_trademark_symbol(blob):
    """Use the registered trademark symbol instead of (R)."""
    err = "BTR103"
    msg = u"(R) is a goofy alphabetic approximation, use the symbol ®."
    regex = "\([rR]\)"

    return existence_check(
        blob, [regex], err, msg, max_errors=3, require_padding=False)


@memoize
def check_sentence_spacing(blob):
    """Use the registered trademark symbol instead of (R)."""
    err = "BTR104"
    msg = u"More than two spaces after the period; use 1 or 2."
    regex = "\. {3}"

    return existence_check(
        blob, [regex], err, msg, max_errors=3, require_padding=False)


# @memoize
# def check_en_dash_separated_names(blob):
#     """Use an en-dash to separate names."""
#     # [u"[A-Z][a-z]{1,10}[-\u2014][A-Z][a-z]{1,10}",
#     #     u"Use an en dash (–) to separate names."],
