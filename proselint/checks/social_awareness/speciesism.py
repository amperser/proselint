"""
Speciesist language.

---
layout:     post
source:     Language and speciesism (Dunayer, 2001); The Political Language of
            Food (Stibbe, 2001); Guidelines for Non-Handicapping Language in
            APA Journals (APA, 1992)
source_url: https://doi.org/10.1080/10350330109384726
title:      speciesist language
date:       2026-02-25
categories: writing
---

Suggests alternatives to common speciesist phrases — idioms and metaphors
that normalize violence toward animals. These phrases reinforce the
treatment of animals as objects, pests, or lesser beings. Clearer,
non-speciesist alternatives exist that are often more precise and more
vivid.

Academic references:
- Dunayer, J. (2001). Animal Equality: Language and Liberation.
- Stibbe, A. (2001). Language, Power, and the Social Construction of
  Animals. Society & Animals, 9(2), 145-161.
- Bogueva, D., & Marinova, D. (2022). Transforming Language About Animals.
  In: Handbook of Research on Social Marketing and Its Influence on Animal
  Origin Food Product Consumption.

"""

from proselint.registry.checks import Check, types

CHECK_PATH = "social_awareness.speciesism"

check_preferred_forms = Check(
    check_type=types.PreferredFormsSimple(
        items={
            "kill two birds with one stone": "solve two problems at once",
            "beat a dead horse": "belabor the point",
            "let the cat out of the bag": "reveal the secret",
            "more than one way to skin a cat": "more than one way to solve it",
            "take the bull by the horns": "take the matter head-on",
            "open a can of worms": "open a Pandora's box",
            "wild goose chase": "futile search",
            "guinea pig": "test subject",
            "be the guinea pig": "be the test subject",
            "like a lamb to the slaughter": "unsuspectingly into danger",
            "flog a dead horse": "belabor the point",
            "hold your horses": "hold on",
            "bring home the bacon": "bring home the pay",
            "put all your eggs in one basket": "risk everything on one venture",
            "like shooting fish in a barrel": "like an easy target",
            "the elephant in the room": "the obvious issue",
            "get your ducks in a row": "get organized",
            "straight from the horse's mouth": "straight from the source",
            "cry crocodile tears": "shed fake tears",
            "has bigger fish to fry": "has bigger things to deal with",
            "dog-eat-dog": "cutthroat",
            "rat race": "daily grind",
            "an albatross around your neck": "a burden to bear",
        }
    ),
    path=CHECK_PATH,
    message=(
        "Speciesist language. Consider using '{}' instead of '{}'."
    ),
)

check_derogatory = Check(
    check_type=types.PreferredFormsSimple(
        items={
            "work like a dog": "work relentlessly",
            "worked like a dog": "worked relentlessly",
            "working like a dog": "working relentlessly",
            "works like a dog": "works relentlessly",
            "drink like a fish": "drink excessively",
            "drinks like a fish": "drinks excessively",
            "eat like a pig": "eat ravenously",
            "eats like a pig": "eats ravenously",
            "eating like a pig": "eating ravenously",
            "sweat like a pig": "sweat profusely",
            "sweating like a pig": "sweating profusely",
            "breed like rabbits": "reproduce quickly",
            "breeding like rabbits": "reproducing quickly",
            "stubborn as a mule": "extremely stubborn",
            "blind as a bat": "completely blind",
            "sly as a fox": "very cunning",
            "busy as a bee": "very busy",
            "crazy as a loon": "out of your mind",
            "proud as a peacock": "extremely proud",
            "quiet as a mouse": "extremely quiet",
            "strong as an ox": "extremely strong",
            "sick as a dog": "very ill",
        }
    ),
    path=CHECK_PATH,
    message=(
        "Speciesist language. This phrase uses an animal comparison "
        "as an insult or stereotype. Consider using '{}' instead of '{}'."
    ),
)

__register__ = (check_preferred_forms, check_derogatory)
