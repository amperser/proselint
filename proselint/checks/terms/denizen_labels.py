"""Denizen labels."""

from __future__ import annotations

from proselint.checks import CheckSpec, PreferredFormsSimple

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "He was definitely a Hong Kongite.",
]

"""
source:     Garner's Modern American Usage
source_url: http://bit.ly/1T4alrY
"""
check = CheckSpec(
    PreferredFormsSimple({
        "Afrikaaner": "Afrikaner",
        "Afrikander": "Afrikaner",
        "Alabaman": "Alabamian",
        "Albuquerquian": "Albuquerquean",
        "Anchoragite": "Anchorageite",
        "Los Angelean": "Angeleno",
        "Arizonian": "Arizonan",
        "Arkansawyer": "Arkansan",
        "Belarusan": "Belarusian",
        "Cayman Islander": "Caymanian",
        "Coloradoan": "Coloradan",
        "Fairbanksian": "Fairbanksan",
        "Fort Worther": "Fort Worthian",
        "Grenadian": "Grenadan",
        "Hong Kongite": "Hong Konger",
        "Hong Kongian": "Hong Konger",
        "Indianan": "Hoosier",
        "Indianian": "Hoosier",
        "Illinoisian": "Illinoisan",
        "Iowegian": "Iowan",
        "Louisianan": "Louisianian",
        "Michiganite": "Michigander",
        "Michiganian": "Michigander",
        "Missouran": "Missourian",
        "Monacan": "Monegasque",
        "Neopolitan": "Neapolitan",
        "New Hampshireite": "New Hampshirite",
        "New Hampshireman": "New Hampshirite",
        "New Jerseyite": "New Jerseyan",
        "New Orleansian": "New Orleanian",
        "Connecticuter": "Nutmegger",
        "Oklahoma Citian": "Oklahoma Cityan",
        "Oklahomian": "Oklahoman",
        "Seattlite": "Seattleite",
        "Surinamer": "Surinamese",
        "Tallahassean": "Tallahasseean",
        "Tennesseean": "Tennessean",
        "Tusconian": "Tusconan",
        "Tusconite": "Tusconan",
        "Utahan": "Utahn",
        "Saudi Arabian": "Saudi",
    }),
    "terms.denizen_labels.garner",
    "'{}' is the preferred denizen label.",
)

"""
source:     Mary Norris
source_url: http://nyr.kr/1rGienj
"""
check_denizen_labels_norris = CheckSpec(
    PreferredFormsSimple({
        "Manchesterian": "Mancunian",
        "Manchesterians": "Mancunians",
        "Valladolidian": "Vallisoletano",
        "Wolverhamptonian": "Wulfrunian",
        "Wolverhamptonite": "Wulfrunian",
        "Newcastleite": "Novocastrian",
        "Newcastlite": "Novocastrian",
        "Trois-Rivièrester": "Trifluvian",
        "Leedsian": "Leodensian",
        "Minneapolisian": "Minneapolitan",
        "Hartlepoolian": "Hartlepudlian",
        "Liverpoolian": "Liverpudlian",
        "Halifaxer": "Haligonian",
        "Warsawer": "Varsovian",
        "Warsawian": "Varsovian",
        "Providencian": "Providentian",
        "Providencer": "Providentian",
        "Trentian": "Tridentine",
        "Trentonian": "Tridentine",
    }),
    "terms.denizen_labels.norris",
    "Would you like '{}'?",
)

__register__ = (
    check,
    check_denizen_labels_norris,
)
