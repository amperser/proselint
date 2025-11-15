"""
Names for groups of animals.

---
layout:     post
source:     Oxford Dictionaries
source_url: http://www.oxforddictionaries.com/words/what-do-you-call-a-group-of
title:      Names for groups of animals
date:       2014-06-10 12:31:19
categories: writing
---

Names for groups of animals.

"""

from collections.abc import Iterator

from proselint.registry.checks import Check, CheckResult, Padding, types

TERM_MAP = (
    ("alligators", "congregation"),
    ("antelopes", "herd"),
    ("baboons", "troop"),
    ("badgers", "cete"),
    ("bats", "colony"),
    ("bears", "sloth"),
    ("buffalo", "herd"),
    ("bullfinches", "bellowing"),
    ("caribou", "herd"),
    ("cats", "glaring"),
    ("caterpillars", "army"),
    ("cockroaches", "intrusion"),
    ("coyotes", "pack"),
    ("crows", "murder"),
    ("dogs", "pack"),
    ("eagles", "convocation"),
    ("emus", "mob"),
    ("flamingos", "stand"),
    ("frogs", "army"),
    ("goldfinches", "charm"),
    ("gorillas", "band"),
    ("guineafowl", "rasp"),
    ("hedgehogs", "array"),
    ("herons", "siege"),
    ("hogs", "parcel"),
    ("hyenas", "cackle"),
    ("ibex", "herd"),
    ("iguanas", "mess"),
    ("lions", "pride"),
    ("locusts", "plague"),
    ("mackerel", "shoal"),
    ("mares", "stud"),
    ("minnows", "shoal"),
    ("moose", "herd"),
    ("mosquitoes", "scourge"),
    ("nightingales", "watch"),
    ("oysters", "bed"),
    ("partridges", "covey"),
    ("pelicans", "pod"),
    ("raccoons", "gaze"),
    ("ravens", "unkindness"),
    ("rhinoceroses", "crash"),
    ("sea urchins", "sea"),
    ("starlings", "murmuration"),
    ("toads", "knot"),
    ("wombats", "wisdom"),
    ("woodcocks", "fall"),
    ("woodpeckers", "descent"),
    ("wrens", "herd"),
)
GENERIC_TERMS = ("group", "bunch")


def _check_venery(text: str, check: Check) -> Iterator[CheckResult]:
    """Check the text."""
    if not check.engine.make_set(Padding.RAW, GENERIC_TERMS).exists_in(text):
        return iter(())

    return types.PreferredFormsSimple(
        items={
            f"{generic} of {animal}": f"{venery} of {animal}"
            for animal, venery in TERM_MAP
            for generic in GENERIC_TERMS
        }
    ).check(text, check)


check_venery = Check(
    check_type=_check_venery,
    path="terms.venery",
    message="The venery term is '{}'.",
)

__register__ = (check_venery,)
