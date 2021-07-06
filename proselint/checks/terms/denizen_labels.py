# -*- coding: utf-8 -*-

"""Denizen labels."""

from proselint.tools import memoize, preferred_forms_check


@memoize
def check(text):
    """Suggest the preferred forms.

    source:     Garner's Modern American Usage
    source_url: http://bit.ly/1T4alrY
    ---
    source:     Mary Norris
    source_url: http://nyr.kr/1rGienj
    """
    err = "terms.denizen_labels.garner"
    msg = "'{}' is the preferred denizen label."

    preferences = [
        # Garner
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
        # Mary Norris
        ["Mancunian",         ["Manchesterian"]],
        ["Mancunians",        ["Manchesterians"]],
        ["Vallisoletano",     ["Valladolidian"]],
        ["Wulfrunian",        ["Wolverhamptonian", "Wolverhamptonite"]],
        ["Novocastrian",      ["Newcastleite", "Newcastlite"]],
        ["Trifluvian",        [u"Trois-Rivièrester"]],
        ["Leodenisian",       ["Leedsian"]],
        ["Minneapolitan",     ["Minneapolisian"]],
        ["Hartlepudlian",     ["Hartlepoolian"]],
        ["Liverpudlian",      ["Liverpoolian"]],
        ["Haligonian",        ["Halifaxer"]],
        ["Varsovian",         ["Warsawer", "Warsawian"]],
        ["Providentian",      ["Providencian", "Providencer"]],
        ["Tridentine",        ["Trentian", "Trentonian"]],
    ]

    return preferred_forms_check(text, preferences, err, msg)
