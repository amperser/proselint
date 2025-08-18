"""Denizen labels."""

from proselint.registry.checks import Check, types

"""
source:     Garner's Modern American Usage
source_url: http://bit.ly/1T4alrY
"""
check_garner = Check(
    check_type=types.PreferredFormsSimple(
        items={
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
    ),
    path="terms.denizen_labels.norris",
    message="Would you like '{}'?",
)

__register__ = (check_garner, check_norris)
