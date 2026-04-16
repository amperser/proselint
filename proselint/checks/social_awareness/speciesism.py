"""
Speciesism.

---
layout:     post
source:     Dunayer, J. (2001). Animal Equality: Language and Liberation.
source_url: https://doi.org/10.1017/S0962728600024489
title:      speciesism
date:       2026-04-08 12:00:00
categories: writing
---

Speciesism is the assumption of human superiority over other animals,
expressed linguistically through idioms that treat animals as objects,
nuisances, or inherently inferior beings. Joan Dunayer's *Animal Equality:
Language and Liberation* (2001) is a foundational academic text examining
how everyday language encodes and reinforces this bias.

This check flags two categories of speciesist language:

1. **Speciesist idioms** — common phrases whose imagery frames animals as
   instruments (e.g. 'kill two birds with one stone'), pests (e.g. 'rat
   race'), or property (e.g. 'cash cow'). Replacing these with neutral
   alternatives improves clarity and avoids reinforcing the view that
   animals exist primarily as means to human ends.

2. **Animal comparisons used as insults** — similes that invoke animals to
   describe human failings (e.g. 'eat like a pig', 'stubborn as a mule').
   These expressions demean both the person and the animal, and clearer
   alternatives are nearly always available.

The idiom list uses Dunayer (2001) as its academic grounding. The specific
phrases included draw on widely recognised speciesist language patterns in
English usage; they are not all direct quotations or enumerated examples
from that text.

"""

from proselint.registry.checks import Check, types

CHECK_PATH = "social_awareness.speciesism"

check_preferred_forms = Check(
    check_type=types.PreferredFormsSimple(
        items={
            "kill two birds with one stone": "solve two problems at once",
            "beat a dead horse": "belabor the point",
            "wild goose chase": "futile search",
            "let the cat out of the bag": "reveal the secret",
            "guinea pig": "test subject",
            "the elephant in the room": "the obvious issue",
            "dog-eat-dog": "cutthroat",
            "rat race": "daily grind",
            "work like a dog": "work relentlessly",
            "more than one way to skin a cat": "more than one way to solve this",
            "open a can of worms": "create a new set of problems",
            "hold your horses": "slow down",
            "dark horse": "unexpected contender",
            "straight from the horse's mouth": "from the original source",
            "flog a dead horse": "belabor the point",
            "take the bull by the horns": "tackle the problem directly",
            "bull in a china shop": "clumsy or disruptive person",
            "sacred cow": "untouchable assumption",
            "cash cow": "reliable revenue source",
            "herding cats": "managing an unruly group",
            "let sleeping dogs lie": "avoid stirring up past trouble",
            "barking up the wrong tree": "pursuing a mistaken course",
            "cat got your tongue": "unable to speak",
            "raining cats and dogs": "raining heavily",
            "bird's-eye view": "aerial view",
            "cold turkey": "abruptly",
        }
    ),
    path=CHECK_PATH,
    message="Speciesist idiom. Consider '{}' instead of '{}'.",
)

check_derogatory = Check(
    check_type=types.PreferredFormsSimple(
        items={
            "eat like a pig": "eat ravenously",
            "stubborn as a mule": "extremely stubborn",
            "blind as a bat": "completely blind",
            "quiet as a mouse": "extremely quiet",
            "drunk as a skunk": "extremely drunk",
            "fat as a pig": "overweight",
            "sweating like a pig": "sweating heavily",
            "slow as a snail": "extremely slow",
            "memory like a goldfish": "short memory",
        }
    ),
    path=CHECK_PATH,
    message="Animal comparison used as an insult. Consider '{}' instead of '{}'.",
)

__register__ = (check_preferred_forms, check_derogatory)
