# -*- coding: utf-8 -*-
"""Denizen labels.

---
layout:     post
source:     Garner's Modern American Usage
source_url: http://amzn.to/15wF76r
title:      denizen labels
date:       2014-06-10 12:31:19
categories: writing
---

Denizen labels.

"""
from tools import memoize, preferred_forms_check


@memoize
def check(text):
    """Suggest the preferred forms."""
    err = "garner.denizen_labels"
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
        ["Caymanian",         ["Cayman Islander"]],
        ["Coloradan",         ["Coloradoan"]],
        ["Fairbanksan",       ["Fairbanksian"]],
        ["Fort Worthian",     ["Fort Worther"]],
        ["Grenadan",          ["Grenadian"]],
        ["Hong Konger",       ["Hong Kongite", "Hong Kongian"]],
        ["Hoosier",           ["Indianan", "Indianian"]],
        ["Illinoisan",        ["Illinoisian"]],
        ["Iowan",             ["Iowegian"]],
        ["Louisianian",       ["Louisianan"]],
        ["Michigander",       ["Michiganite", "Michiganian"]],
        ["Missourian",        ["Missouran"]],
        ["Monegasque",        ["Monacan"]],
        ["Neapolitan",        ["Neopolitan"]],
        ["New Hampshirite",   ["New Hampshireite", "New Hampshireman"]],
        ["New Jerseyan",      ["New Jerseyite"]],
        ["New Orleanian",     ["New Orleansian"]],
        ["Nutmegger",         ["Connecticuter"]],
        ["Oklahoma Cityan",   ["Oklahoma Citian"]],
        ["Oklahoman",         ["Oklahomian"]],
        ["Seattleite",        ["Seattlite"]],
        ["Surinamese",        ["Surinamer"]],
        ["Tallahasseean",     ["Tallahassean"]],
        ["Tennessean",        ["Tennesseean"]],
        ["Tusconan",          ["Tusconian", "Tusconite"]],
        ["Utahn",             ["Utahan"]],
        ["Saudi",             ["Saudi Arabian"]],
    ]

    return preferred_forms_check(text, preferences, err, msg)
