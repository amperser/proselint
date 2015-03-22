# -*- coding: utf-8 -*-
"""MAU109: Denizen labels.

---
layout:     post
error_code: MAU109
source:     Garner's Modern American Usage
source_url: http://amzn.to/15wF76r
title:      denizen labels
date:       2014-06-10 12:31:19
categories: writing
---

Denizen labels.

"""
from proselint.tools import memoize, preferred_forms_check


@memoize
def check(blob):
    """Suggest the preferred forms."""
    err = "MAU109"
    msg = "'{}' is the preferred denizen label."

    preferences = [

        ["Afrikaner",         ["Afrikaaner"]],
        ["Afrikaner",         ["Afrikander"]],
        ["Alabamian",         ["Alabaman"]],
        ["Albuquerquean",     ["Albuquerquian"]],
        ["Anchorageite",      ["Anchoragite"]],
        ["Angeleno",          ["Los Angelean"]],
        ["Arizonan",          ["Arizonian"]],
        ["Arkansan",          ["Arkansawyer"]],
        ["Belarusian",        ["Belarusan"]],
        ["Coloradan",         ["Coloradoan"]],
        ["Fairbanksan",       ["Fairbanksian"]],
        ["Fort Worthian",     ["Fort Worther"]],
        ["Hong Konger",       ["Hong Kongite", "Hong Kongian"]],
        ["Hoosier",           ["Indianan", "Indianian"]],
        ["Illinoisan",        ["Illinoisian"]],
        ["Iowan",             ["Iowegian"]],
        ["Louisianian",       ["Louisianan"]],
        ["Michigander",       ["Michiganite", "Michiganian"]],
        ["Missourian",        ["Missouran"]],
        ["Monegasque",        ["Monacan"]],
        ["Neapolitan",        ["Neopolitan"]],
        ["Saudi",             ["Saudi Arabian"]],
    ]

    return preferred_forms_check(blob, preferences, err, msg)
