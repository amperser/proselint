# -*- coding: utf-8 -*-
"""Psychological and psychiatric terms to avoid.

---
layout:     post
source:     Scott O. Lilienfeld, et al.
source_url: http://dx.doi.org/10.3389/fpsyg.2015.01100
title:      psychological and psychiatric terms to avoid
date:       2014-06-10 12:31:19
categories: writing
---

Psychological and psychiatric terms to avoid.

"""
from proselint.tools import preferred_forms_check, existence_check, memoize


@memoize
def check(text):
    """Suggest the preferred forms."""
    err = "psychology.lie_detector"
    msg = "Polygraph machines measure arousal, not lying per se. Try {}."

    list = [
        ["polygraph test",      ["lie detector test"]],
        ["polygraph machine",   ["lie detector machine"]],
    ]

    return preferred_forms_check(text, list, err, msg)


