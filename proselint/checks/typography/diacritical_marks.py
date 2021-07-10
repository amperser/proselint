"""Diacritical marks.

Use of diacritical marks where common.
"""
from proselint.tools import memoize, preferred_forms_check


@memoize
def check(text):
    """Suggest the preferred forms."""
    err = "typography.diacritical_marks"
    msg = "Use diacritical marks in '{}'."

    list = [
        # French loanwords
        ["beau idéal",         ["beau ideal"]],
        ["boutonnière",        ["boutonniere"]],
        ["bric-à-brac",        ["bric-a-brac"]],
        ["café",               ["cafe"]],
        ["cause célèbre",      ["cause celebre"]],
        ["chèvre",             ["chevre"]],
        ["cliché",             ["cliche"]],
        ["comme ci comme ça",  ["comme ci comme ca", "comsi comsa"]],
        ["consommé",           ["consomme"]],
        ["coup d'état",        ["coup d'etat"]],
        ["coup de grâce",      ["coup de grace"]],
        ["crudités",           ["crudites"]],
        ["crème brûlée",       ["creme brulee"]],
        ["crème de menthe",    ["creme de menthe"]],
        ["crème fraîche",      ["creme fraice"]],
        ["crème fraîche",      ["creme fresh"]],
        ["crêpe",              ["crepe"]],
        ["débutante",          ["debutante"]],
        ["décor",              ["decor"]],
        ["déjà vu",            ["deja vu"]],
        ["dénouement",         ["denouement"]],
        ["façade",             ["facade"]],
        ["fiancé",             ["fiance"]],
        ["fiancée",            ["fiancee"]],
        ["flambé",             ["flambe"]],
        ["garçon",             ["garcon"]],
        ["lycée",              ["lycee"]],
        ["maître d",           ["maitre d"]],
        ["ménage à trois",     ["menage a trois"]],
        ["négligée",           ["negligee"]],
        ["papier-mâché", ["papier-mache", "paper mache", "paper-mache"]],
        ["protégé",            ["protege"]],
        ["protégée",           ["protegee"]],
        ["purée",              ["puree"]],
        ["raison d'être",      ["raison d'etre"]],
        ["my résumé",          ["my resume"]],
        ["your résumé",        ["your resume"]],
        ["his résumé",         ["his resume"]],
        ["her résumé",         ["her resume"]],
        ["a résumé",           ["a resume"]],
        ["the résumé",         ["the resume"]],
        ["risqué",             ["risque"]],
        ["roué",               ["roue"]],
        ["soirée",             ["soiree"]],
        ["soufflé",            ["souffle"]],
        ["soupçon",            ["soupcon"]],
        ["touché",             ["touche"]],
        ["tête-à-tête",        ["tete-a-tete"]],
        ["voilà",              ["voila"]],
        ["à la carte",         ["a la carte"]],
        ["à la mode",          ["a la mode"]],
        ["émigré",             ["emigre"]],

        # Spanish loanwords
        ["El Niño",            ["El Nino"]],
        ["jalapeño",           ["jalapeno"]],
        ["La Niña",            ["La Nina"]],
        ["piña colada",        ["pina colada"]],
        ["señor",              ["senor"]],
        ["señora",             ["senora"]],
        ["señorita",           ["senorita"]],

        # Portuguese loanwords
        ["açaí",               ["acai"]],

        # German loanwords
        ["doppelgänger",       ["doppelganger"]],
        ["Führer",             ["Fuhrer"]],
        ["Gewürztraminer",     ["Gewurztraminer"]],
        ["vis-à-vis",          ["vis-a-vis"]],
        ["Übermensch",         ["Ubermensch"]],

        # Swedish loanwords
        ["filmjölk",           ["filmjolk"]],
        ["smörgåsbord",        ["smorgasbord"]],

        # Names, places, and companies
        ["Beyoncé",            ["Beyonce"]],
        ["Brontë",             ["Bronte"]],
        ["Brontë",             ["Bronte"]],
        ["Champs-Élysées",     ["Champs-Elysees"]],
        ["Citroën",            ["Citroen"]],
        ["Curaçao",            ["Curacao"]],
        ["Häagen-Dazs",        ["Haagen-Dazs", "Haagen Dazs"]],
        ["Löwenbräu",          ["Lowenbrau"]],
        ["Monégasque",         ["Monegasque"]],
        ["Mötley Crüe",        ["Motley Crue"]],
        ["Nescafé",            ["Nescafe"]],
        ["Queensrÿche",        ["Queensryche"]],
        ["Québec",             ["Quebec"]],
        ["Québécois",          ["Quebecois"]],
        ["Ångström",           ["Angstrom"]],
        ["ångström",           ["angstrom"]],
        ["Škoda",              ["Skoda"]],
    ]

    return preferred_forms_check(text, list, err, msg)
