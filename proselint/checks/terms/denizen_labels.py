"""Denizen labels."""

from proselint.registry.checks import Check, types

"""
source:     Garner's Modern American Usage
source_url: http://bit.ly/1T4alrY
"""
check_garner = Check(
    check_type=types.PreferredFormsSimple(
        items={
            "afrikaaner": "Afrikaner",
            "afrikander": "Afrikaner",
            "alabaman": "Alabamian",
            "albuquerquian": "Albuquerquean",
            "anchoragite": "Anchorageite",
            "los Angelean": "Angeleno",
            "arizonian": "Arizonan",
            "arkansawyer": "Arkansan",
            "belarusan": "Belarusian",
            "cayman islander": "Caymanian",
            "coloradoan": "Coloradan",
            "fairbanksian": "Fairbanksan",
            "fort worther": "Fort Worthian",
            "grenadian": "Grenadan",
            "hong kongite": "Hong Konger",
            "hong kongian": "Hong Konger",
            "indianan": "Hoosier",
            "indianian": "Hoosier",
            "illinoisian": "Illinoisan",
            "iowegian": "Iowan",
            "louisianan": "Louisianian",
            "michiganite": "Michigander",
            "michiganian": "Michigander",
            "missouran": "Missourian",
            "monacan": "Monegasque",
            "neopolitan": "Neapolitan",
            "new hampshireite": "New Hampshirite",
            "new hampshireman": "New Hampshirite",
            "new jerseyite": "New Jerseyan",
            "new orleansian": "New Orleanian",
            "connecticuter": "Nutmegger",
            "oklahoma citian": "Oklahoma Cityan",
            "oklahomian": "Oklahoman",
            "seattlite": "Seattleite",
            "surinamer": "Surinamese",
            "tallahassean": "Tallahasseean",
            "tennesseean": "Tennessean",
            "tusconian": "Tusconan",
            "tusconite": "Tusconan",
            "utahan": "Utahn",
            "saudi arabian": "Saudi",
        }
    ),
    path="terms.denizen_labels.garner",
    message="'{}' is the preferred denizen label.",
)

"""
source:     Mary Norris
source_url: http://nyr.kr/1rGienj
"""
check_norris = Check(
    check_type=types.PreferredFormsSimple(
        items={
            "manchesterian": "Mancunian",
            "manchesterians": "Mancunians",
            "valladolidian": "Vallisoletano",
            "wolverhamptonian": "Wulfrunian",
            "wolverhamptonite": "Wulfrunian",
            "newcastleite": "Novocastrian",
            "newcastlite": "Novocastrian",
            "trois-rivièrester": "Trifluvian",
            "leedsian": "Leodenisian",
            "minneapolisian": "Minneapolitan",
            "hartlepoolian": "Hartlepudlian",
            "liverpoolian": "Liverpudlian",
            "halifaxer": "Haligonian",
            "warsawer": "Varsovian",
            "warsawian": "Varsovian",
            "providencian": "Providentian",
            "providencer": "Providentian",
            "trentian": "Tridentine",
            "trentonian": "Tridentine",
        }
    ),
    path="terms.denizen_labels.norris",
    message="Would you like '{}'?",
)

__register__ = (check_garner, check_norris)
