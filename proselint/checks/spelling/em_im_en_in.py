# -*- coding: utf-8 -*-

"""Em vs. im, en vs. in."""

from proselint.tools import memoize, preferred_forms_check


@memoize
def check_em_vs_em_and_en_vs_in(text):
    """em- vs. en-, im- vs. in-."""
    err = "spelling.em_im_en_in"
    msg = "em-, im-, en-, and in-. '{}' is the preferred spelling."

    preferences = [

        ["embalm",      ["imbalm"]],
        ["embark",      ["imbark"]],
        ["embed",       ["imbed"]],
        ["embitter",    ["imbitter"]],
        ["emblaze",     ["imblaze"]],
        ["embody",      ["imbody"]],
        ["embolden",    ["imbolden"]],
        ["embosom",     ["imbosom"]],
        ["embower",     ["imbower"]],
        ["embrown",     ["imbrown"]],
        ["empanel",     ["impanel"]],
        ["empower",     ["impower"]],
        ["encage",      ["incage"]],
        ["encapsulate", ["incapsulate"]],
        ["encase",      ["incase"]],
        ["enclasp",     ["inclasp"]],
        ["encumber",    ["incumber"]],
        ["encumbrance", ["incumbrance"]],
        ["endow",       ["indow"]],
        ["endowment",   ["indowment"]],
        ["endue",       ["indue"]],
        ["enfold",      ["infold"]],
        ["engraft",     ["ingraft"]],
        ["engulf",      ["ingulf"]],
        ["enlace",      ["inlace"]],
        ["enmesh",      ["inmesh"]],
        ["ensheathe",   ["insheathe"]],
        ["enshrine",    ["inshrine"]],
        ["ensnare",     ["insnare"]],
        ["ensoul",      ["insoul"]],
        ["ensphere",    ["insphere"]],
        ["enthrall",    ["inthrall"]],
        ["enthrone",    ["inthrone"]],
        ["entitle",     ["intitle"]],
        ["entomb",      ["intomb"]],
        ["entreat",     ["intreat"]],
        ["entrench",    ["intrench"]],
        ["entrust",     ["intrust"]],
        ["entwine",     ["intwine"]],
        ["entwist",     ["intwist"]],
        ["enwind",      ["inwind"]],
        ["enwrap",      ["inwrap"]],
        ["enwreathe",   ["inwreathe"]],
        ["imbrue",      ["embrue"]],
        ["impale",      ["empale"]],
        ["impoverish",  ["empoverish"]],
        ["inflame",     ["enflame"]],
        ["ingrain",     ["engrain"]],
        ["inure",       ["enure"]],
    ]

    return preferred_forms_check(text, preferences, err, msg)
