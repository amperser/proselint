# -*- coding: utf-8 -*-

"""Redundancy."""

from proselint.tools import memoize, preferred_forms_check


@memoize
def check(text):
    """Suggest the preferred forms."""
    err = "redundancy.wallace"
    msg = "Redundancy. Use '{}' instead of '{}'."

    redundancies = [
        ["rectangular",        ["rectangular in shape"]],
        ["audible",            ["audible to the ear"]],
    ]
    return preferred_forms_check(text, redundancies, err, msg)


@memoize
def check_garner(text):
    """Suggest the preferred forms.

    source:     Garner's Modern American Usage
    source_url: http://bit.ly/1T4alrY
    """
    err = "redundancy.garner"
    msg = "Redundancy. Use '{}' instead of '{}'."

    redundancies = [
        ["adequate",          ["adequate enough"]],
        ["admitted",          ["self-admitted"]],
        ["affidavit",         ["sworn affidavit"]],
        ["agreement",         ["mutual agreement"]],
        ["alumnus",           ["former alumnus"]],
        ["antithetical",      ["directly antithetical"]],
        ["approximately",     ["approximately about"]],
        ["associate",         ["associate together(?: in groups)?"]],
        ["bivouac",           ["temporary bivouac", "bivouac camp"]],
        ["blend",             ["blend together"]],
        ["but",               ["but nevertheless"]],
        ["charged with...",   ["accused of a charge"]],
        ["circumstances of",  ["circumstances surrounding"]],
        ["circumstances",     ["surrounding circumstances"]],
        ["close",             ["close proximity"]],
        ["collaborate",       ["collaborate together"]],
        ["collaborator",      ["fellow collaborator"]],
        ["collaborators",     ["fellow collaborators"]],
        ["collocated",        ["collocated together"]],
        ["colleagues",        ["fellow colleagues"]],
        ["combine",           ["combine together"]],
        ["complacent",        ["self-complacent"]],
        ["confessed",         ["self-confessed"]],
        ["connect",           ["connect together"]],
        ["consensus",         ["(?:general )?consensus of opinion"]],
        ["consolidate",       ["consolidate together"]],
        ["continues to",      ["still continues to"]],
        ["contradictory",     ["mutually contradictory"]],
        ["cooperation",       ["mutual cooperation"]],
        ["couple",            ["couple together"]],
        ["crisis",            ["serious crisis"]],
        ["eliminate",         ["entirely eliminate"]],
        ["especially",        ["most especially"]],
        ["fact",              ["actual fact"]],
        ["facts",             ["true facts"]],
        ["forecast",          ["future forecast"]],
        ["founding fathers",  ["founding forefathers"]],
        ["free",              ["free and gratis"]],
        ["free",              ["free gratis"]],
        ["full",              ["completely full"]],
        ["fundamentals",      ["basic fundamentals"]],
        ["gift",              ["free gift"]],
        ["innovation",        ["new innovation"]],
        ["interact",          ["interact with each other"]],
        ["large",             ["large-size"]],
        ["meld",              ["meld together"]],
        ["merge",             ["merge together"]],
        ["mingle",            ["mingle together"]],
        ["mix",               ["mix together"]],
        ["mutual feelings",   ["mutual feelings for eachother"]],
        ["mutual respect",    ["mutual respect for each other"]],
        ["native citizen",    ["native-born citizen"]],
        ["necessity",         ["absolute necessity"]],
        ["obvious",           ["blatantly obvious"]],
        ["pause",             ["pause for a moment"]],
        ["planning",          ["advance planning"]],
        ["plans",             ["future plans"]],
        ["pooled",            ["pooled together"]],
        ["potable water",     ["potable drinking water"]],
        ["potable water",     ["potable drinking water"]],
        ["recruit",           ["new recruit"]],
        ["reelected",         ["reelected for another term"]],
        ["refer",             ["refer back"]],
        ["regress",           ["regress back"]],
        ["repay them",        ["repay them back"]],
        ["repay",             ["repay back"]],
        ["repeat",            ["repeat again"]],
        ["repeat",            ["repeat back"]],
        ["repeat",            ["repeat the same"]],
        ["repeated",          ["repeated the same"]],
        ["reprieve",          ["temporary reprieve"]],
        ["respite",           ["brief respite"]],
        ["retirement",        ["retiral", "retiracy"]],
        ["retreat",           ["retreat back"]],
        ["return",            ["return back"]],
        ["scrutinize",        ["closely scrutinize"]],
        ["software",          ["software program"]],
        ["surrounded",        ["surrounded on all sides"]],
        ["the nation",        ["the whole entire nation"]],
        ["throughout the",    ["throughout the entire"]],
        ["timpani",           ["timpani drum"]],
        ["twins",             ["pair of twins"]],
        ["vacancy",           ["unfilled vacancy"]],
        ["various",           ["various different"]],
        ["veteran",           ["former veteran"]],
        ["visible",           ["visible to the eye"]],
        ["vocation",          ["professional vocation"]],
        ["while",             ["while at the same time"]],
    ]

    return preferred_forms_check(text, redundancies, err, msg)


@memoize
def check_nordquist(text):
    """Suggest the preferred forms.

    source:     Richard Nordquist
    source_url: http://grammar.about.com/bio/Richard-Nordquist-22176.htm
    """
    err = "redundancy.nordquist"
    msg = "Redundancy. Use '{}' instead of '{}'."

    redundancies = [
        ["essential",          ["absolutely essential"]],
        ["necessary",          ["absolutely necessary"]],
        ["a.m.",               ["a.m. in the morning"]],
        ["p.m.",               ["p.m. at night"]],
    ]
    return preferred_forms_check(text, redundancies, err, msg)
