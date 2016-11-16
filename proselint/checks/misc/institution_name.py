# -*- coding: utf-8 -*-
"""Common errors with institution names.

---
layout:     post
source:     Institution's webpage
source_url: http://bit.ly/2en1zbv,
title:      Institution Name
date:       2016-11-16 11:46:19
categories: writing
---

Institution names.

"""
from proselint.tools import memoize, preferred_forms_check


@memoize
def check_vtech(text):
    """Suggest the correct name.

    source: Virginia Tech Division of Student Affairs
    source_url: http://bit.ly/2en1zbv
    """
    err = "institution.vtech"
    msg = "Incorrect name. Use '{}' instead of '{}'."

    institution = [
        ["Virginia Polytechnic Institute and State University",
         ["Virginia Polytechnic and State University"]],
    ]
    return preferred_forms_check(text, institution, err, msg)
