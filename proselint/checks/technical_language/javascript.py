# -*- coding: utf-8 -*-
"""Technical language.

---
layout:     post
source:     technical-word-rules
source_url: https://github.com/azu/technical-word-rules
title:      techincal language
date:       2016-09-12 12:31:19
categories: writing
---

Points out technical expressions that are written incorrectly

"""
from proselint.tools import memoize, preferred_forms_check, existence_check

@memoize
def check(text):
    """Suggest preferred forms."""
    err = "technical_language.javascript"
    msg = "Incorrect form. Use '{}' instead of '{}'."

    technical_language = [
        ["ECMAScript #",       ["ECMAScript([0-9]+)"]], #TODO
        ["ES.next",             ["ES next"]],
        # ["Web Components",      ["WebComponents", "web components", "Web components"]],
        ["localStorage",        ["localstorage"]],
        # ["sessionStorage",      ["session storage|sessionstorage"]],
        # ["HTML Imports",        ["HTML Import"]],
        ["JavaScript",          ["Java Script"]],
        # ["Pointer Events",      ["pointer event"]],
        # ["Touch Events",      ["touch event"]],
        ["Ember.js",            ["EmberJS"]]
    ]
    
    errors = preferred_forms_check(text, technical_language, err, msg, ignore_case=False)
    
    check_caps = [ 
        "ES6 Classes", 
        "JavaScript",
        "Web Audio API"
    ]
    check_caps_lower = [x.lower() for x in check_caps]
    
    for m in existence_check(text, check_caps, err, "{}", ignore_case=True):
        original = m[3]
        if original not in check_caps: 
            correct = check_caps[check_caps_lower.index(original.lower())]
            errors.append((
                m[0],
                m[1],
                m[2],
                msg.format(correct, original),
                None))

    return errors
