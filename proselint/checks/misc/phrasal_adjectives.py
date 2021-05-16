# -*- coding: utf-8 -*-
"""Phrasal adjectives.

---
layout:     post
source:     Garner's Modern American Usage
source_url: http://bit.ly/1T4alrY
title:      Phrasal adjectives
date:       2014-06-10 12:31:19
categories: writing
---

Phrasal adjectives.

"""
from proselint.tools import existence_check, preferred_forms_check, memoize


@memoize
def check_ly(text):
    """Check the text."""
    err = "garner.phrasal_adjectives.ly"
    msg = u"""No hyphen is necessary in phrasal adjectives with an adverb
              ending in -ly, unless the -ly adverb is part of a longer
              phrase"""

    regex = r"\s[^\s-]+ly-"

    return existence_check(text, [regex], err, msg,
                           require_padding=False, offset=-1)


@memoize
def check(text):
    """Check the text."""
    err = "garner.phrasal_adjectives.examples"
    msg = u"""Hyphenate '{1}', a phrasal adjective, as '{0}'."""

    list = [
        ["across-the-board discounts", ["across the board discounts"]],
        ["acute-care treatment", ["acute care treatment"]],
        ["agreed-upon answer", ["agreed upon answer"]],
        ["big-ticket item", ["big ticket item"]],
        ["class-action lawyer", ["class action lawyer"]],
        ["criminal-law professor", ["criminal law professor"]],
        ["cut-and-dried issue", ["cut and dried issue"]],
        ["downward-sloping line", ["downward sloping line"]],
        ["English-language learners", ["English language learners"]],
        ["English-speaking people", ["English speaking people"]],
        ["even-numbered", ["even numbered"]],
        ["face-to-face meeting", ["fact to face meeting"]],
        ["fixed-rate mortgage", ["fixed rate mortgage"]],
        ["for-profit firm", ["for profit firm"]],
        ["foreign-sounding name", ["foreign sounding name"]],
        ["government-owned business", ["government owned business"]],
        ["hard-and-fast issue", ["hard and fast issue"]],
        ["head-on collision", ["head on collision"]],
        ["head-to-head battle", ["head to head battle"]],
        ["head-to-head competition", ["head to head competition"]],
        ["health-care coverage", ["heath care coverage"]],
        ["high-school student", ["high school student"]],
        ["hit-and-run statute", ["hit and run statute"]],
        ["HIV-negative person", ["HIV negative person"]],
        ["HIV-positive person", ["HIV positive person"]],
        ["information-technology personnel",
            ["information technology personnel"]],
        ["intellectual-property rights", ["intellectual property rights"]],
        ["interest-group pressures", ["interest group pressures"]],
        ["joint-stock company", ["joint stock company"]],
        ["kidney-dialysis machine", ["kidney dialysis machine"]],
        ["long-run costs", ["long run costs"]],
        ["long-term care", ["long term care"]],
        ["low-income housing", ["low income housing"]],
        ["mom-and-pop retail outlet", ["mom and pop retail outlet"]],
        ["mom-and-pop shop", ["mom and pop shop"]],
        ["national-security briefing", ["national security briefing"]],
        ["natural-gas pipeline", ["natural gas pipeline"]],
        ["no-fault accident", ["no fault accident"]],
        ["no-fault divorce", ["no fault divorce"]],
        ["no-fault insurance", ["no fault insurance"]],
        ["odd-numbered", ["odd numbered"]],
        ["office-supply store", ["office supply store"]],
        ["one-way flight", ["one way flight"]],
        ["one-way window", ["one way window"]],
        ["open-and-shut case", ["open and shut case"]],
        ["open-and-shut issue", ["open and shut issue"]],
        ["open-source community", ["open source community"]],
        ["optical-scan ballot", ["optical scan ballot"]],
        ["pension-fund investments", ["pension fund investments"]],
        ["private-sector employment", ["private sector employment"]],
        ["profit-seeking efforts", ["profit seeking efforts"]],
        ["punch-card ballot", ["punch card ballot"]],
        ["quality-adjusted price", ["quality adjusted price"]],
        ["razor-sharp intellect", ["razor sharp intellect"]],
        ["razor-sharp mind", ["razor sharp mind"]],
        ["razor-sharp mind", ["razor sharp mind"]],
        ["razor-sharp wit", ["razor sharp wit"]],
        ["larger-than-life personality", ["larger than life personality"]],
        ["real-estate prices", ["real estate prices"]],
        ["real-estate tycoon", ["real estate tycoon"]],
        ["right-wing militia", ["right wing militia"]],
        ["round-trip flight", ["round trip flight"]],
        ["search-and-rescue operation", ["search and rescue operation"]],
        ["second-largest army", ["second largest army"]],
        ["shell-shocked mothers", ["shell shocked mothers"]],
        ["shell-shocked soldiers", ["shell shocked soldiers"]],
        ["small-business loan", ["small business loan"]],
        ["small-business owner", ["small business owner"]],
        ["small-state senator", ["small state senator"]],
        ["small-animal veterinarian", ["small animal veterinarian"]],
        ["state-sponsored terrorism", ["state sponsored terrorism"]],
        ["state-sponsored violence", ["state sponsored violence"]],
        ["thumbs-up sign", ["thumbs up sign"]],
        ["time-honored tradition", ["time honored tradition"]],
        ["U.S.-led campaign", ["U.S. led campaign"]],
        ["upward-sloping line", ["upward sloping line"]],
        ["venture-backed company", ["venture backed company"]],
        ["well-publicized event", ["well publicized event"]],
        ["wire-transfer service", ["wire transfer service"]],
        ["yes-or-no question", ["yes or no question"]],
        ["zero-sum game", ["zero sum game"]],
        ["stained-glass ceiling", ["stained glass ceiling"]],
        ["stained-glass window", ["stained glass window"]],
        ["free-range chicken", ["free range chicken"]],
        ["free-range poultry", ["free range poultry"]],
        ["non-profit-making organization",
            ["non profit making organization",
             "non-profit making organization",
             "non profit-making organization"]],


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
