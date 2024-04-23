"""Denizen labels."""

from __future__ import annotations

from proselint.checks import CheckResult
from proselint.checks import preferred_forms_check_opti

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "He was definitely a Hong Kongite.",
]


def check(text: str) -> list[CheckResult]:
    """Suggest the preferred forms.

    source:     Garner's Modern American Usage
    source_url: http://bit.ly/1T4alrY
    """
    err = "terms.denizen_labels.garner"
    msg = "'{}' is the preferred denizen label."

    items: dict[str, str] = {
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
    }

    return preferred_forms_check_opti(text, items, err, msg)


def check_denizen_labels_norris(text: str) -> list[CheckResult]:
    """Suggest the preferred forms.

    source:     Mary Norris
    source_url: http://nyr.kr/1rGienj
    """
    err = "terms.denizen_labels.norris"
    msg = "Would you like '{}'?"

    items: dict[str, str] = {
        "Manchesterian": "Mancunian",
        "Manchesterians": "Mancunians",
        "Valladolidian": "Vallisoletano",
        "Wolverhamptonian": "Wulfrunian",
        "Wolverhamptonite": "Wulfrunian",
        "Newcastleite": "Novocastrian",
        "Newcastlite": "Novocastrian",
        "Trois-Rivièrester": "Trifluvian",
        "Leedsian": "Leodenisian",
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
    }

    return preferred_forms_check_opti(text, items, err, msg)
