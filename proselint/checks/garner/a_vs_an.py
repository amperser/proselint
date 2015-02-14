# -*- coding: utf-8 -*-
u"""MAU100: Misuse of 'a' vs. 'an'.

---
layout:     post
error_code: MAU101
source:     Garner's Modern American Usage
source_url: http://amzn.to/15wF76r
title:      a vs. an
date:       2014-06-10 12:31:19
categories: writing
---

The first line is always wrong.

"""
import re
from proselint.tools import memoize
import os


@memoize
def check(text):
    """Define the check."""
    err = "MAU101"
    msg_a = "'a' should be 'an'."
    msg_an = "'an' should be 'a'."

    errors = []
    regex = re.compile("(?:^|\W)(an?)\s+(\w+)", re.IGNORECASE)

    # Find all occurences of the regex in the text.
    for g in regex.finditer(text):
        words = [w for w in g.groups()]

        vowel_sound = starts_with_vowel_sound(words[1])

        if vowel_sound is None:
            continue

        # A apple.
        if words[0] in ["A", "a"] and vowel_sound:
            errors.append((g.start(), g.start() + 1, err, msg_a))

        # An day.
        elif words[0] in ["An", "an"] and not vowel_sound:
            errors.append((g.start(), g.start() + 2, err, msg_an))

    return errors


@memoize
def starts_with_vowel_sound(word):
    """Check whether the word starts with a vowel sound."""
    # Get the pronunciations of the word.
    if 'd' not in globals():
        import nltk
        nltk.data.path.append(
            os.path.join(
                os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
                "data"))
        global d
        d = nltk.corpus.cmudict.dict()

    pronunciations = d.get(word)
    if pronunciations is None:
        return None

    # For each pronunciation, see if it starts with a vowel sound.
    is_vowel = [p[0][-1].isdigit() for p in pronunciations]

    # Return the appropriate value only if all the pronunciations match.
    if all(is_vowel):
        return True
    elif not any(is_vowel):
        return False
    else:
        return None


def initialize():
    """Initialize the cache of pronunciations."""
    print "Running initialization for garner.a_vs_an (may take a few minutes)"
    from nltk.corpus import cmudict

    global d
    d = cmudict.dict()

    for i, word in enumerate(d):
        starts_with_vowel_sound(word)
        if not (i % 1000):
            print i

    assert(d)
