# -*- coding: utf-8 -*-
"""PKR100: Metadiscourse.

---
layout:     post
error_code: PKR100
source:     Pinker's book on writing
source_url: ???
title:      metadiscourse
date:       2014-06-10 12:31:19
categories: writing
---

Points out metadiscourse.

"""
from proselint.tools import memoize, existence_check


@memoize
def check(blob):
    """Suggest the preferred forms."""
    err = "PKR100"
    msg = "Excessive metadiscourse."

    metadiscourse = [
        "The preceeding discussion",
        "The rest of this article",
        "This chapter discusses",
        "The preceding paragraph demonstrated",
        "The previous section analyzed",
    ]

    return existence_check(blob, metadiscourse, err, msg)
