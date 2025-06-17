"""
Metadiscourse.

---
layout:     post
source:     Pinker's book on writing
source_url: ???
title:      metadiscourse
date:       2014-06-10 12:31:19
categories: writing
---

Points out metadiscourse.

"""

from proselint.registry.checks import Check, types

check = Check(
    check_type=types.Existence(
        items=(
            "The preceeding discussion",
            "The rest of this article",
            "This chapter discusses",
            "The preceding paragraph demonstrated",
            "The previous section analyzed",
        )
    ),
    path="misc.metadiscourse",
    message="Excessive metadiscourse.",
)

__register__ = (check,)
