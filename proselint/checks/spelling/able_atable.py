# -*- coding: utf-8 -*-

"""-able vs. -atable."""

from proselint.tools import memoize, preferred_forms_check


@memoize
def check(text):
    """-able vs. -atable."""
    err = "spelling.able_atable"
    msg = "-able vs. -atable. '{}' is the preferred spelling."

    preferences = [

        ["abbreviable",       ["abbreviatable"]],
        ["abdicable",         ["abdicatable"]],
        ["abrogable",         ["abrogatable"]],
        ["accommodable",      ["accommodatable"]],
        ["accumulable",       ["accumulatable"]],
        ["activable",         ["activatable"]],
        ["administrable",     ["administratable"]],
        ["adulterable",       ["adulteratable"]],
        ["affiliable",        ["affiliatable"]],
        ["aggregable",        ["aggregatable"]],
        ["agitable",          ["agitatable"]],
        ["alienable",         ["alienatable"]],
        ["alleviable",        ["alleviatable"]],
        ["allocable",         ["allocatable"]],
        ["ameliorable",       ["amelioratable"]],
        ["annihilable",       ["annihilatable"]],
        ["appreciable",       ["appreciatable"]],
        ["appropriable",      ["appropriatable"]],
        ["arbitrable",        ["arbitratable"]],
        ["articulable",       ["articulatable"]],
        ["calculable",        ["calculatable"]],
        ["communicable",      ["communicatable"]],
        ["compensable",       ["compensatable"]],
        ["confiscable",       ["confiscatable"]],
        ["corroborable",      ["corroboratable"]],
        ["cultivable",        ["cultivatable"]],
        ["delegable",         ["delegatable"]],
        ["delineable",        ["delineatable"]],
        ["demonstrable",      ["demonstratable"]],
        ["detonable",         ["detonatable"]],
        ["differentiable",    ["differentiatable"]],
        ["eradicable",        ["eradicatable"]],
        ["evacuable",         ["evacuatable"]],
        ["evaluable",         ["evaluatable"]],
        ["expropriable",      ["expropriatable"]],
        ["generable",         ["generatable"]],
        ["indicable",         ["indicatable"]],
        ["inebriable",        ["inebriatable"]],
        ["inextirpable",      ["inextirpatable"]],
        ["inextricable",      ["inextricatable"]],
        ["infatuable",        ["infatuatable"]],
        ["infuriable",        ["infuriatable"]],
        ["invalidable",       ["invalidatable"]],
        ["investigable",      ["investigatable"]],
        ["isolable",          ["isolatable"]],
        ["litigable",         ["litigatable"]],
        ["manipulable",       ["manipulatable"]],
        ["medicable",         ["medicatable"]],
        ["navigable",         ["navigatable"]],
        ["obligable",         ["obligatable"]],
        ["obviable",          ["obviatable"]],
        ["operable",          ["operatable"]],
        ["originable",        ["originatable"]],
        ["participable",      ["participatable"]],
        ["penetrable",        ["penetratable"]],
        ["perpetrable",       ["perpetratable"]],
        ["perpetuable",       ["perpetuatable"]],
        ["predicable",        ["predicatable"]],
        ["propagable",        ["propagatable"]],
        ["regulable",         ["regulatable"]],
        ["replicable",        ["replicatable"]],
        ["repudiable",        ["repudiatable"]],
        ["segregable",        ["segregatable"]],
        ["separable",         ["separatable"]],
        ["subjugable",        ["subjugatable"]],
        ["vindicable",        ["vindicatable"]],
        ["violable",          ["violatable"]],
        ["vitiable",          ["vitiatable"]]
    ]

    return preferred_forms_check(text, preferences, err, msg)
