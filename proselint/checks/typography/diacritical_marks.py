"""
Diacritical marks.

Use of diacritical marks where common.
"""

from proselint.registry.checks import Check, types

check = Check(
    check_type=types.PreferredFormsSimple(
        items={
            # French loanwords
            "cafe": "café",
            "cliche": "cliché",
            "crepe": "crêpe",
            "decor": "décor",
            "facade": "façade",
            "fiance": "fiancé",
            "flambe": "flambé",
            "garcon": "garçon",
            "protege": "protégé",
            "puree": "purée",
            "risque": "risqué",
            "roue": "roué",
            "soiree": "soirée",
            "souffle": "soufflé",
            "touche": "touché",
            "voila": "voilà",
            "resume": "résumé",
            "chevre": "chèvre",
            "consomme": "consommé",
            "creme fraice": "crème fraîche",
            "creme fresh": "crème fraîche",
            "creme brulee": "crème brûlée",
            "creme de menthe": "crème de menthe",
            "debutante": "débutante",
            "deja vu": "déjà vu",
            "denouement": "dénouement",
            "fiancee": "fiancée",
            "lycee": "lycée",
            "maitre d": "maître d",
            "negligee": "négligée",
            "papier-mache": "papier-mâché",
            "paper mache": "papier-mâché",
            "paper-mache": "papier-mâché",
            "protegee": "protégée",
            "raison d'etre": "raison d'être",
            "soupcon": "soupçon",
            "tete-a-tete": "tête-à-tête",
            "a la carte": "à la carte",
            "a la mode": "à la mode",
            "emigre": "émigré",
            "vis-a-vis": "vis-à-vis",
            "cause celebre": "cause célèbre",
            "coup d'etat": "coup d'état",
            "coup de grace": "coup de grâce",
            "crudites": "crudités",
            "bric-a-brac": "bric-à-brac",
            "beau ideal": "beau idéal",
            "comme ci comme ca": "comme ci comme ça",
            "comsi comsa": "comme ci comme ça",
            "menage a trois": "ménage à trois",
            # Spanish loanwords
            "senor": "señor",
            "senora": "señora",
            "el nino": "El Niño",
            "la nina": "La Niña",
            "senorita": "señorita",
            "jalapeno": "jalapeño",
            "pina colada": "piña colada",
            # Portuguese loanwords
            "acai": "açaí",
            # German loanwords
            "fuhrer": "Führer",
            "ubermensch": "Übermensch",
            "doppelganger": "doppelgänger",
            "gewurztraminer": "Gewürztraminer",
            # Swedish loanwords
            "filmjolk": "filmjölk",
            "smorgasbord": "smörgåsbord",
            # Names, places, and companies
            "skoda": "Škoda",
            "quebec": "Québec",
            "bronte": "Brontë",
            "beyonce": "Beyoncé",
            "curacao": "Curaçao",
            "nescafe": "Nescafé",
            "citroen": "Citroën",
            "angstrom": "Ångström",
            "quebecois": "Québécois",
            "lowenbrau": "Löwenbräu",
            "monegasque": "Monégasque",
            "motley crue": "Mötley Crüe",
            "haagen-dazs": "Häagen-Dazs",
            "haagen dazs": "Häagen-Dazs",
            "queensryche": "Queensrÿche",
            "champs-elysees": "Champs-Élysées",
        }
    ),
    path="typography.diacritical_marks",
    message="Use diacritical marks in '{}'.",
)

__register__ = (check,)
