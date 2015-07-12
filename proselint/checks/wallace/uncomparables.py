# -*- coding: utf-8 -*-
u"""Comparing uncomparables.

---
layout:     post
source:     David Foster Wallace
source_url: http://www.telegraph.co.uk/a/9715551
title:      Comparing an uncomparable
date:       2014-06-10 12:31:19
categories: writing
---

David Foster Wallace says:

> This is one of a class of adjectives, sometimes called “uncomparables”, that
can be a little tricky. Among other uncomparables are precise, exact, correct,
entire, accurate, preferable, inevitable, possible, false; there are probably
two dozen in all. These adjectives all describe absolute, non-negotiable
states: something is either false or it’s not; something is either inevitable
or it’s not. Many writers get careless and try to modify uncomparables with
comparatives like more and less or intensives like very. But if you really
think about them, the core assertions in sentences like “War is becoming
increasingly inevitable as Middle East tensions rise”; “Their cost estimate was
more accurate than the other firms’”; and “As a mortician, he has a very unique
attitude” are nonsense. If something is inevitable, it is bound to happen; it
cannot be bound to happen and then somehow even more bound to happen. Unique
already means one-of-a-kind, so the adj. phrase very unique is at best
redundant and at worst stupid, like “audible to the ear” or “rectangular in
shape”. You can blame the culture of marketing for some of this difficulty.
As the number and rhetorical volume of US ads increase, we become inured to
hyperbolic language, which then forces marketers to load superlatives and
uncomparables with high-octane modifiers (special - very special -
Super-special! - Mega-Special!!), and so on. A deeper issue implicit in the
problem of uncomparables is the dissimilarities between Standard Written
English and the language of advertising. Advertising English, which probably
deserves to be studied as its own dialect, operates under different syntactic
rules than SWE, mainly because AE’s goals and assumptions are different.
Sentences like “We offer a totally unique dining experience”; “Come on down and
receive your free gift”; and “Save up to 50 per cent… and more!” are perfectly
OK in Advertising English — but this is because Advertising English is aimed at
people who are not paying close attention. If your audience is by definition
involuntary, distracted and numbed, then free gift and totally unique stand a
better chance of penetrating — and simple penetration is what AE is all about.
One axiom of Standard Written English is that your reader is paying close
attention and expects you to have done the same.
"""
import re
from proselint.tools import memoize
import itertools


@memoize
def check(text):
    """Check the text."""
    err = "wallace.uncomparables"
    msg = "Comparison of an uncomparable: '{}' is not comparable."

    comparators = [
        "most",
        "more",
        "less",
        "least",
        "very",
        "quite",
        "largely",
        "extremely",
        "increasingly"
    ]

    uncomparables = [
        "absolute",
        "adequate",
        "chief",
        "complete",
        "correct",
        "devoid",
        "entire",
        "false",
        "fatal",
        "favorite",
        "final",
        "ideal",
        "impossible",
        "inevitable",
        "infinite",
        "irrevocable",
        "main",
        "manifest",
        "only",
        "paramount",
        "perfect",
        "perpetual",
        "possible",
        "preferable",
        "principal",
        "singular",
        "stationary",
        "sufficient",
        "true",
        "unanimous",
        "unavoidable",
        "unbroken",
        "uniform",
        "unique",
        "universal",
        "void",
        "whole",
    ]

    exceptions = [
        ("more", "perfect"),
        ("more", "possible")  # FIXME
    ]

    all = ["\\b" + i[0] + "\s" + i[1] + "[\W$]" for i in itertools.product(
           comparators, uncomparables) if i not in exceptions]

    occ = re.finditer("|".join(all), text.lower())
    return [(o.start(), o.end(), err, msg.format(o.group(0))) for o in occ]
