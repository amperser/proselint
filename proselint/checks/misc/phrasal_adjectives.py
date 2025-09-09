"""
Phrasal adjectives.

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

from proselint.registry.checks import Check, types

check_ly = Check(
    check_type=types.ExistenceSimple(pattern=r"\s[^\s-]+ly-"),
    path="misc.phrasal_adjectives.ly",
    message=(
        "No hyphen is necessary in phrasal adjectives with an adverb"
        " ending in -ly, unless the -ly adverb is part of a longer phrase."
    ),
    offset=(1, 0),
)

check = Check(
    check_type=types.PreferredFormsSimple(
        items={
            "across the board discounts": "across-the-board discounts",
            "acute care treatment": "acute-care treatment",
            "agreed upon answer": "agreed-upon answer",
            "big ticket item": "big-ticket item",
            "class action lawyer": "class-action lawyer",
            "criminal law professor": "criminal-law professor",
            "cut and dried issue": "cut-and-dried issue",
            "downward sloping line": "downward-sloping line",
            "english language learners": "English-language learners",
            "english speaking people": "English-speaking people",
            "even numbered": "even-numbered",
            "fact to face meeting": "face-to-face meeting",
            "fixed rate mortgage": "fixed-rate mortgage",
            "for profit firm": "for-profit firm",
            "foreign sounding name": "foreign-sounding name",
            "free range chicken": "free-range chicken",
            "free range poultry": "free-range poultry",
            "government owned business": "government-owned business",
            "hard and fast issue": "hard-and-fast issue",
            "head on collision": "head-on collision",
            "head to head battle": "head-to-head battle",
            "head to head competition": "head-to-head competition",
            "heath care coverage": "health-care coverage",
            "high school student": "high-school student",
            "hit and run statute": "hit-and-run statute",
            "hiv negative person": "HIV-negative person",
            "hiv positive person": "HIV-positive person",
            "information technology personnel": (
                "information-technology personnel"
            ),
            "intellectual property rights": "intellectual-property rights",
            "interest group pressures": "interest-group pressures",
            "joint stock company": "joint-stock company",
            "kidney dialysis machine": "kidney-dialysis machine",
            "larger than life personality": "larger-than-life personality",
            "long run costs": "long-run costs",
            "long term care": "long-term care",
            "low income housing": "low-income housing",
            "mom and pop retail outlet": "mom-and-pop retail outlet",
            "mom and pop shop": "mom-and-pop shop",
            "national security briefing": "national-security briefing",
            "natural gas pipeline": "natural-gas pipeline",
            "no fault accident": "no-fault accident",
            "no fault divorce": "no-fault divorce",
            "no fault insurance": "no-fault insurance",
            "non profit making organization": "non-profit-making organization",
            "non profit-making organization": "non-profit-making organization",
            "non-profit making organization": "non-profit-making organization",
            "odd numbered": "odd-numbered",
            "office supply store": "office-supply store",
            "one way flight": "one-way flight",
            "one way window": "one-way window",
            "open and shut case": "open-and-shut case",
            "open and shut issue": "open-and-shut issue",
            "open source community": "open-source community",
            "optical scan ballot": "optical-scan ballot",
            "pension fund investments": "pension-fund investments",
            "private sector employment": "private-sector employment",
            "profit seeking efforts": "profit-seeking efforts",
            "punch card ballot": "punch-card ballot",
            "quality adjusted price": "quality-adjusted price",
            "razor sharp intellect": "razor-sharp intellect",
            "razor sharp mind": "razor-sharp mind",
            "razor sharp wit": "razor-sharp wit",
            "real estate prices": "real-estate prices",
            "real estate tycoon": "real-estate tycoon",
            "right wing militia": "right-wing militia",
            "round trip flight": "round-trip flight",
            "search and rescue operation": "search-and-rescue operation",
            "second largest army": "second-largest army",
            "shell shocked mothers": "shell-shocked mothers",
            "shell shocked soldiers": "shell-shocked soldiers",
            "small animal veterinarian": "small-animal veterinarian",
            "small business loan": "small-business loan",
            "small business owner": "small-business owner",
            "small state senator": "small-state senator",
            "stained glass ceiling": "stained-glass ceiling",
            "stained glass window": "stained-glass window",
            "state sponsored terrorism": "state-sponsored terrorism",
            "state sponsored violence": "state-sponsored violence",
            "thumbs up sign": "thumbs-up sign",
            "time honored tradition": "time-honored tradition",
            "upward sloping line": "upward-sloping line",
            "venture backed company": "venture-backed company",
            "well publicized event": "well-publicized event",
            "wire transfer service": "wire-transfer service",
            "yes or no question": "yes-or-no question",
            "zero sum game": "zero-sum game",
            r"u\.s\. led campaign": r"U\.S\.-led campaign",
            # Harmony
            "three part harmony": "three-part harmony",
            "four part harmony": "four-part harmony",
            "six part harmony": "six-part harmony",
            "eight part harmony": "eight-part harmony",
            # Losses and gains.
            "first quarter gain": "first-quarter gain",
            "first quarter loss": "first-quarter loss",
            "second quarter gain": "second-quarter gain",
            "second quarter loss": "second-quarter loss",
            "third quarter gain": "third-quarter gain",
            "third quarter loss": "third-quarter loss",
            "fourth quarter gain": "fourth-quarter gain",
            "fourth quarter loss": "fourth-quarter loss",
        }
    ),
    path="misc.phrasal_adjectives.examples",
    message="""Hyphenate '{1}', a phrasal adjective, as '{0}'.""",
)

__register__ = (check_ly, check)
