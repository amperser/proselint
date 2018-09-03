"""Weasel words.

---
layout:     post
source:     write-good
source_url:
http://matt.might.net/articles/
 shell-scripts-for-passive-voice-weasel-words-duplicates/
title:      Weasel words.
date:       2014-06-10 12:31:19
categories: writing
---

Weasel words clearly weaken various aspects of a number of your sentences.

"""
from proselint.tools import memoize, existence_check


@memoize
def check(text):
    """Avoid using weasel words in technical writing."""
    err = "weasel_words.misc"
    msg = "Avoid using weasel words."
    words = [
        "many",
        "various",
        "farily",
        "several different",
        "extremely",
        "exceedingly",
        "quite",
        "remarkably",
        "surprisingly",
        "mostly",
        "largely",
        "interestingly",
        "significantly",
        "substantially",
        "clearly",
        "vast",
        "relatively",
        "compeletely"
    ]

    return existence_check(text, words, err, msg, max_errors=1)
