# -*- coding: utf-8 -*-
"""Phrasal adjectives.

---
layout:     post
source:     Garner's Modern American Usage
source_url: http://amzn.to/15wF76r
title:      Phrasal adjectives
date:       2014-06-10 12:31:19
categories: writing
---

Phrasal adjectives.

"""
from tools import existence_check, preferred_forms_check, memoize


@memoize
def check_ly(text):
    """Check the text."""
    err = "garner.phrasal_adjectives.ly"
    msg = u"""No hyphen is necessary in phrasal adjectives with an adverb
              ending in -ly."""

    return existence_check(text, ["ly-"], err, msg,
                           require_padding=False, offset=-1)


@memoize
def check_examples(text):
    """Check the text."""
    err = "garner.phrasal_adjectives.examples"
    msg = u"""Hyphenate '{}', a phrasal adjective, as '{}'."""

    list = [
        ["across-the-board discounts", ["across the board discounts"]],
        ["acute-care treatment", ["acute care treatment"]],
        ["agreed-upon answer", ["agreed upon answer"]],
        ["big-ticket item", ["big ticket item"]],
        ["class-action lawyer", ["class action lawyer"]],
        ["English-speaking people", ["English speaking people"]],
        ["high-school student", ["high school student"]],
        ["one-way flight", ["one way flight"]],
        ["right-wing militia", ["right wing militia"]],
        ["round-trip flight", ["round trip flight"]],
        ["search-and-rescue operation", ["search and rescue operation"]],
        ["second-largest army", ["second largest army"]],
        ["shell-shocked mothers", ["shell shocked mothers"]],
        ["shell-shocked soldiers", ["shell shocked soldiers"]],
        ["state-sponsored terrorism", ["state sponsored terrorism"]],
        ["state-sponsored violence", ["state sponsored violence"]],
        ["U.S.-led campaign", ["U.S. led campaign"]],
        ["venture-backed company", ["venture backed company"]],
        ["wire-transfer service", ["wire transfer service"]],
        ["real-estate prices", ["real estate prices"]],
        ["punch-card ballot", ["punch card ballot"]],
        ["private-sector employment", ["private sector employment"]],
        ["optical-scan ballot", ["optical scan ballot"]],
        ["natural-gas pipeline", ["natural gas pipeline"]],
        ["national-security briefing", ["national security briefing"]],
        ["mom-and-pop shop", ["mom and pop shop"]],
        ["mom-and-pop retail outlet", ["mom and pop retail outlet"]],
        ["low-income housing", ["low income housing"]],
        ["health-care coverage", ["heath care coverage"]],
        ["zero-sum game", ["zero sum game"]],
        ["yes-or-no question", ["yes or no question"]],
        ["time-honored tradition", ["time honored tradition"]],
        ["small-business loan", ["small business loan"]],
        ["razor-sharp mind", ["razor sharp mind"]],
        ["quality-adjusted price", ["quality adjusted price"]],
        ["profit-seeking efforts", ["profit seeking efforts"]],
        ["one-way window", ["one way window"]],
        ["pension-fund investments", "pension fund investments"],
        ["odd-numbered", ["odd numbered"]],
        ["even-numbered", ["even numbered"]],
        ["office-supply store", ["office supply store"]],
        ["no-fault accident", ["no fault accident"]],
        ["no-fault divorce", ["no fault divorce"]],
        ["no-fault insurance", ["no fault insurance"]],
        ["well-publicized event", ["well publicized event"]],
        ["thumbs-up sign", ["thumbs up sign"]],
        ["razor-sharp mind", ["razor sharp mind"]],
        ["razor-sharp intellect", ["razor sharp intellect"]],
        ["long-term care", ["long term care"]],
        ["long-run costs", ["long run costs"]],
        ["kidney-dialysis machine", ["kidney dialysis machine"]],
        ["joint-stock company", ["joint stock company"]],
        ["interest-group pressures", ["interest group pressures"]],
        ["intellectual-property rights", ["intellectual property rights"]],
        ["information-technology personnel",
            ["information technology personnel"]],
        ["HIV-negative person", ["HIV negative person"]],
        ["HIV-positive person", ["HIV positive person"]],
        ["hit-and-run statute", ["hit and run statute"]],
        ["head-on collision", ["head on collision"]],
        ["head-to-head competition", ["head to head competition"]],
        ["head-to-head battle", ["head to head battle"]],
        ["hard-and-fast issue", ["hard and fast issue"]],
        ["cut-and-dried issue", ["cut and dried issue"]],
        ["open-and-shut issue", ["open and shut issue"]],
        ["open-and-shut case", ["open and shut case"]],
        ["government-owned business", ["government owned business"]],
        ["for-profit firm", ["for profit firm"]],
        ["face-to-face meeting", ["fact to face meeting"]],
        ["foreign-sounding name", ["foreign sounding name"]],
        ["downward-sloping line", ["downward sloping line"]],
        ["upward-sloping line", ["upward sloping line"]],

        # Harmony
        ["three-part harmony", ["three part harmony"]],
        ["four-part harmony", ["four part harmony"]],
        ["six-part harmony", ["six part harmony"]],
        ["eight-part harmony", ["eight part harmony"]],

        # Losses and gains.
        ["first-quarter loss", ["first quarter loss"]],
        ["second-quarter loss", ["second quarter loss"]],
        ["third-quarter loss", ["third quarter loss"]],
        ["fourth-quarter loss", ["fourth quarter loss"]],
        ["first-quarter gain", ["first quarter gain"]],
        ["second-quarter gain", ["second quarter gain"]],
        ["third-quarter gain", ["third quarter gain"]],
        ["fourth-quarter gain", ["fourth quarter gain"]],

    ]

    return preferred_forms_check(text, list, err, msg)
