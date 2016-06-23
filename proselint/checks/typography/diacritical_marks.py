# -*- coding: utf-8 -*-
"""Diacritical marks.

Use of diacritical marks where common.
"""
from proselint.tools import memoize, preferred_forms_check


@memoize
def check(text):
    """Suggest the preferred forms."""
    err = "typography.diacritical_marks"
    msg = u"Use diacritical marks in '{}'."

    list = [
        # French loanwords
        [u"beau idéal",         ["beau ideal"]],
        [u"boutonnière",        ["boutonniere"]],
        [u"bric-à-brac",        ["bric-a-brac"]],
        [u"café",               ["cafe"]],
        [u"cause célèbre",      ["cause celebre"]],
        [u"chèvre",             ["chevre"]],
        [u"cliché",             ["cliche"]],
        [u"comme ci comme ça",  ["comme ci comme ca", "comsi comsa"]],
        [u"consommé",           ["consomme"]],
        [u"coup d'état",        ["coup d'etat"]],
        [u"coup de grâce",      ["coup de grace"]],
        [u"crudités",           ["crudites"]],
        [u"crème brûlée",       ["creme brulee"]],
        [u"crème de menthe",    ["creme de menthe"]],
        [u"crème fraîche",      ["creme fraice"]],
        [u"crème fraîche",      ["creme fresh"]],
        [u"crêpe",              ["crepe"]],
        [u"débutante",          ["debutante"]],
        [u"décor",              ["decor"]],
        [u"déjà vu",            ["deja vu"]],
        [u"dénouement",         ["denouement"]],
        [u"façade",             ["facade"]],
        [u"fiancé",             ["fiance"]],
        [u"fiancée",            ["fiancee"]],
        [u"flambé",             ["flambe"]],
        [u"garçon",             ["garcon"]],
        [u"lycée",              ["lycee"]],
        [u"maître d",           ["maitre d"]],
        [u"ménage à trois",     ["menage a trois"]],
        [u"négligée",           ["negligee"]],
        [u"papier-mâché", ["papier-mache", "paper mache", "paper-mache"]],
        [u"protégé",            ["protege"]],
        [u"protégée",           ["protegee"]],
        [u"purée",              ["puree"]],
        [u"raison d'être",      ["raison d'etre"]],
        [u"my résumé",          ["my resume"]],
        [u"your résumé",        ["your resume"]],
        [u"his résumé",         ["his resume"]],
        [u"her résumé",         ["her resume"]],
        [u"a résumé",           ["a resume"]],
        [u"the résumé",         ["the resume"]],
        [u"risqué",             ["risque"]],
        [u"roué",               ["roue"]],
        [u"soirée",             ["soiree"]],
        [u"soufflé",            ["souffle"]],
        [u"soupçon",            ["soupcon"]],
        [u"touché",             ["touche"]],
        [u"tête-à-tête",        ["tete-a-tete"]],
        [u"voilà",              ["voila"]],
        [u"à la carte",         ["a la carte"]],
        [u"à la mode",          ["a la mode"]],
        [u"émigré",             ["emigre"]],

        # Spanish loanwords
        [u"El Niño",            ["El Nino"]],
        [u"jalapeño",           ["jalapeno"]],
        [u"La Niña",            ["La Nina"]],
        [u"piña colada",        ["pina colada"]],
        [u"señor",              ["senor"]],
        [u"señora",             ["senora"]],
        [u"señorita",           ["senorita"]],

        # Portuguese loanwords
        [u"açaí",               ["acai"]],

        # German loanwords
        [u"doppelgänger",       ["doppelganger"]],
        [u"Führer",             ["Fuhrer"]],
        [u"Gewürztraminer",     ["Gewurztraminer"]],
        [u"vis-à-vis",          ["vis-a-vis"]],
        [u"Übermensch",         ["Ubermensch"]],

        # Swedish loanwords
        [u"filmjölk",           ["filmjolk"]],
        [u"smörgåsbord",        ["smorgasbord"]],

        # Names, places, and companies
        [u"Beyoncé",            ["Beyonce"]],
        [u"Brontë",             ["Bronte"]],
        [u"Brontë",             ["Bronte"]],
        [u"Champs-Élysées",     ["Champs-Elysees"]],
        [u"Citroën",            ["Citroen"]],
        [u"Curaçao",            ["Curacao"]],
        [u"Häagen-Dazs",        ["Haagen-Dazs", "Haagen Dazs"]],
        [u"Löwenbräu",          ["Lowenbrau"]],
        [u"Monégasque",         ["Monegasque"]],
        [u"Mötley Crüe",        ["Motley Crue"]],
        [u"Nescafé",            ["Nescafe"]],
        [u"Queensrÿche",        ["Queensryche"]],
        [u"Québec",             ["Quebec"]],
        [u"Québécois",          ["Quebecois"]],
        [u"Ångström",           ["Angstrom"]],
        [u"ångström",           ["angstrom"]],
        [u"Škoda",              ["Skoda"]],
    ]

    return preferred_forms_check(text, list, err, msg)
