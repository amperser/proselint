"""
Diacritical marks.

Use of diacritical marks where common.
"""
from __future__ import annotations

from proselint.checks import CheckResult, preferred_forms_check_opti

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "He saw the performance by Beyonce.",
]


def check(text: str) -> list[CheckResult]:
    """Suggest the preferred forms."""
    err = "typography.diacritical_marks"
    msg = "Use diacritical marks in '{}'."

    items: dict[str, str] = {
        # French loanwords
        "beau ideal": "beau idéal",
        "boutonniere": "boutonnière",
        "bric-a-brac": "bric-à-brac",
        "cafe": "café",
        "cause celebre": "cause célèbre",
        "chevre": "chèvre",
        "cliche": "cliché",
        "comme ci comme ca": "comme ci comme ça",
        "comsi comsa": "comme ci comme ça",
        "consomme": "consommé",
        "coup d'etat": "coup d'état",
        "coup de grace": "coup de grâce",
        "crudites": "crudités",
        "creme brulee": "crème brûlée",
        "creme de menthe": "crème de menthe",
        "creme fraice": "crème fraîche",
        "creme fresh": "crème fraîche",
        "crepe": "crêpe",
        "debutante": "débutante",
        "decor": "décor",
        "deja vu": "déjà vu",
        "denouement": "dénouement",
        "facade": "façade",
        "fiance": "fiancé",
        "fiancee": "fiancée",
        "flambe": "flambé",
        "garcon": "garçon",
        "lycee": "lycée",
        "maitre d": "maître d",
        "menage a trois": "ménage à trois",
        "negligee": "négligée",
        "papier-mache": "papier-mâché",
        "paper mache": "papier-mâché",
        "paper-mache": "papier-mâché",
        "protege": "protégé",
        "protegee": "protégée",
        "puree": "purée",
        "raison d'etre": "raison d'être",
        "my resume": "my résumé",
        "your resume": "your résumé",
        "his resume": "his résumé",
        "her resume": "her résumé",
        "a resume": "a résumé",
        "the resume": "the résumé",
        "risque": "risqué",
        "roue": "roué",
        "soiree": "soirée",
        "souffle": "soufflé",
        "soupcon": "soupçon",
        "touche": "touché",
        "tete-a-tete": "tête-à-tête",
        "voila": "voilà",
        "a la carte": "à la carte",
        "a la mode": "à la mode",
        "emigre": "émigré",
        # Spanish loanwords
        "El Nino": "El Niño",
        "jalapeno": "jalapeño",
        "La Nina": "La Niña",
        "pina colada": "piña colada",
        "senor": "señor",
        "senora": "señora",
        "senorita": "señorita",
        # Portuguese loanwords
        "acai": "açaí",
        # German loanwords
        "doppelganger": "doppelgänger",
        "Fuhrer": "Führer",
        "Gewurztraminer": "Gewürztraminer",
        "vis-a-vis": "vis-à-vis",
        "Ubermensch": "Übermensch",
        # Swedish loanwords
        "filmjolk": "filmjölk",
        "smorgasbord": "smörgåsbord",
        # Names, places, and companies
        "Beyonce": "Beyoncé",
        "Bronte": "Brontë",
        "Champs-Elysees": "Champs-Élysées",
        "Citroen": "Citroën",
        "Curacao": "Curaçao",
        "Haagen-Dazs": "Häagen-Dazs",
        "Haagen Dazs": "Häagen-Dazs",
        "Lowenbrau": "Löwenbräu",
        "Monegasque": "Monégasque",
        "Motley Crue": "Mötley Crüe",
        "Nescafe": "Nescafé",
        "Queensryche": "Queensrÿche",
        "Quebec": "Québec",
        "Quebecois": "Québécois",
        "Angstrom": "Ångström",
        "angstrom": "ångström",
        "Skoda": "Škoda",
    }

    return preferred_forms_check_opti(text, items, err, msg)
