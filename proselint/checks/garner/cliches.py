# -*- coding: utf-8 -*-
u"""Cliches.

---
layout:     post
source:     Garner's Modern American Usage
source_url: http://amzn.to/15wF76r
title:      a vs. an
date:       2014-06-10 12:31:19
categories: writing
---

Cliches are cliché.

"""
from tools import memoize, existence_check


@memoize
def check(text):
    """Check the text."""
    err = "garner.cliches"
    msg = u"'{}' is cliché."

    cliches = [
        "a fate worse than death",
        "alas and alack",
        "at the end of the day",
        "bald-faced lie",
        "between a rock and a hard place",
        "between Scylla and Charybdis",
        "between the devil and the deep blue see",
        "betwixt and between",
        "blissful ignorance",
        "blow a fuse",
        "bulk large",
        "but that's another story",
        "cast aspersions",
        "chase a red herring",
        "comparing apples and oranges",
        "compleat",
        "conspicuous by its absence",
        "crystal clear",
        "cutting edge",
        "decision-making process",
        "dubious distinction",
        "duly authorized",
        "eyes peeled",
        "far be it from me",
        "fast and loose",
        "fills the bill",
        "first and foremost",
        "for free",
        "get with the program",
        "gilding the lily",
        "have a short fuse",
        "he's got his hands full",
        "his own worst enemy",
        "his work cut out for him",
        "hither and yon",
        "Hobson's choice",
        "horns of a dilemma",
        "if you catch my drift",
        "in light of",
        "in the final analysis",
        "in the last analysis",
        "innocent bystander",
        "it's not what you know, it's who you know",
        "last but not least",
        "make a mockery of",
        "male chauvinism",
        "moment of truth",
        "more in sorrow than in anger",
        "more sinned against than sinning",
        "my better half",
        "nip in the bud",
        "olden days",
        "on the same page",
        "presidential timber",
        "pulled no punches",
        "quantum jump",
        "quantum leap",
        "redound to one's credit",
        "redound to the benefit of",
        "sea change",
        "shirked his duties",
        "six of one, half a dozen of the other",
        "stretched to the breaking point",
        "than you can shake a stick at",
        "the cream of the crop",
        "the cream rises to the top",
        "the straw that broke the camel's back",
        "thick as thieves",
        "thinking outside the box",
        "thought leaders?",
        "throw the baby out with the bathwater",
        "various and sundry",
        "viable alternative",
        "wax eloquent",
        "wax poetic",
        "we've got a situation here",
        "whet (?:the|your) appetite",
        "wool pulled over our eyes",
        "writ large",
    ]
    return existence_check(text, cliches, err, msg, join=True)
