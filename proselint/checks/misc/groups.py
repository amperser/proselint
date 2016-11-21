# -*- coding: utf-8 -*-
"""Proper/alternative terms for specific types of groups.

---
layout:     post
source:     Oxford Dictionaries
source_url: http://bit.ly/2fIhb8O
title:      groups
date:       2016-09-20 12:35:00
categories: writing
---

Terms for specific types of groups.

"""
from proselint.tools import memoize, preferred_forms_check


# Allow multiple generic group terms
def make_list(terms, group):
    return [group.format(term) for term in terms]


@memoize
def check(text):
    """Suggest the preferred forms."""
    err = "groups"
    msg = "You can use '{}' instead of the generic grouping used in '{}'."
    terms = ["group", "bunch"]

    preferences = [
        # People
        ["blush",           make_list(terms=terms, group="{} of boys")],
        ["drunkship",       make_list(terms=terms, group="{} of cobblers")],
        ["hastiness",       make_list(terms=terms, group="{} of cooks")],
        ["stalk",           make_list(terms=terms, group="{} of foresters")],
        ["observance",      make_list(terms=terms, group="{} of hermits")],
        ["bevy",            make_list(terms=terms, group="{} of ladies")],
        ["faith",           make_list(terms=terms, group="{} of merchants")],
        ["superfluity",     make_list(terms=terms, group="{} of nuns")],
        ["malapertness",    make_list(terms=terms, group="{} of pedlars")],
        ["pity",            make_list(terms=terms, group="{} of prisoners")],
        ["glozing",         make_list(terms=terms, group="{} of taverners")],

        # Animals
        ["shrewdness",      make_list(terms=terms, group="{} of apes")],
        ["herd or pace",    make_list(terms=terms, group="{} of asses")],
        ["troop",           make_list(terms=terms, group="{} of baboons")],
        ["cete",            make_list(terms=terms, group="{} of badgers")],
        ["sloth",           make_list(terms=terms, group="{} of bears")],
        ["swarm, drift, or hive", make_list(terms=terms, group="{} of bees")],
        ["flock, flight, or pod", make_list(terms=terms, group="{} of birds")],
        ["herd, gang, or obstinacy",
         make_list(terms=terms, group="{} of buffalo")],
        ["bellowing",       make_list(terms=terms, group="{} of bullfinches")],
        ["drove",           make_list(terms=terms, group="{} of bullocks")],
        ["army",        make_list(terms=terms, group="{} of caterpillars")],
        ["clowder or glaring", make_list(terms=terms, group="{} of cats")],
        ["herd or drove",   make_list(terms=terms, group="{} of cattle")],
        ["brood, clutch, or peep",
         make_list(terms=terms, group="{} of chickens")],
        ["chattering or clattering", make_list(terms=terms,
                                               group="{} of choughs")],
        ["rag or rake",     make_list(terms=terms, group="{} of colts")],
        ["covert",          make_list(terms=terms, group="{} of coots")],
        ["herd",            make_list(terms=terms, group="{} of cranes")],
        ["crocodiles",      make_list(terms=terms, group="{} of crocodiles")],
        ["murder",          make_list(terms=terms, group="{} of crows")],
        ["litter",          make_list(terms=terms, group="{} of cubs")],
        ["herd",            make_list(terms=terms, group="{} of curlew")],
        ["cowardice",       make_list(terms=terms, group="{} of curs")],
        ["herd or mob",     make_list(terms=terms, group="{} of deer")],
        ["pack or kennel",  make_list(terms=terms, group="{} of dogs")],
        ["school",          make_list(terms=terms, group="{} of dolphins")],
        ["trip",            make_list(terms=terms, group="{} of dotterel")],
        ["flight, dole, or piteousness",
         make_list(terms=terms, group="{} of doves")],
        ["raft, bunch, or paddling (if on water), safe (if on land)",
         make_list(terms=terms, group="{} of ducks")],
        ["fling",           make_list(terms=terms, group="{} of dunlins")],
        ["herd or parade",  make_list(terms=terms, group="{} of elephants")],
        ["gang or herd",    make_list(terms=terms, group="{} of elk")],
        ["busyness",        make_list(terms=terms, group="{} of ferrets")],
        ["charm or chirm",  make_list(terms=terms, group="{} of finches")],
        ["shoal or run",    make_list(terms=terms, group="{} of fish")],
        ["swarm or cloud",  make_list(terms=terms, group="{} of flies")],
        ["skulk",           make_list(terms=terms, group="{} of foxes")],
        ["gaggle (if on land), skein or team or wedge (if in flight)",
         make_list(terms=terms, group="{} of geese")],
        ["herd",            make_list(terms=terms, group="{} of giraffes")],
        ["cloud",           make_list(terms=terms, group="{} of gnats")],
        ["flock, herd or trip",
         make_list(terms=terms, group="{} of goats")],
        ["band",            make_list(terms=terms, group="{} of gorillas")],
        ["pack or convey",  make_list(terms=terms, group="{} of grouse")],
        ["down, mute, or husk", make_list(terms=terms, group="{} of hares")],
        ["cast",            make_list(terms=terms, group="{} of hawks")],
        ["siege",           make_list(terms=terms, group="{} of herons")],
        ["bloat",           make_list(terms=terms, group="{} of hippopotami")],
        ["drove, sting, stud, or team",
         make_list(terms=terms, group="{} of horses")],
        ["pack, cry, or kennel", make_list(terms=terms, group="{} of hounds")],
        ["flight or swarm", make_list(terms=terms, group="{} of insects")],
        ["fluther or smack", make_list(terms=terms, group="{} of jellyfish")],
        ["mob or troop",    make_list(terms=terms, group="{} of kangaroos")],
        ["kindle or litter", make_list(terms=terms, group="{} of kittens")],
        ["desert",          make_list(terms=terms, group="{} of lapwing")],
        ["exaltation or bevy",  make_list(terms=terms, group="{} of larks")],
        ["leap or pepe",    make_list(terms=terms, group="{} of leopards")],
        ["pride or sawt",   make_list(terms=terms, group="{} of lions")],
        ["tiding",          make_list(terms=terms, group="{} of magpies")],
        ["sord or suit",    make_list(terms=terms, group="{} of mallard")],
        ["stud",            make_list(terms=terms, group="{} of mares")],
        ["richesse",        make_list(terms=terms, group="{} of martens")],
        ["labour",          make_list(terms=terms, group="{} of moles")],
        ["troop",           make_list(terms=terms, group="{} of monkeys")],
        ["barren",          make_list(terms=terms, group="{} of mules")],
        ["watch",
         make_list(terms=terms, group="{} of nightingales")],
        ["yoke",            make_list(terms=terms, group="{} of oxen")],
        ["pandemonium",     make_list(terms=terms, group="{} of parrots")],
        ["covey",           make_list(terms=terms, group="{} of partridges")],
        ["muster",          make_list(terms=terms, group="{} of peacocks")],
        ["muster, parcel, or rookery",
         make_list(terms=terms, group="{} of penguins")],
        ["head or nye",     make_list(terms=terms, group="{} of pheasants")],
        ["kit",             make_list(terms=terms, group="{} of pigeons")],
        ["litter",          make_list(terms=terms, group="{} of pigs")],
        ["stand, wing, or congregation",
         make_list(terms=terms, group="{} of plovers")],
        ["rush or flight",  make_list(terms=terms, group="{} of pochards")],
        ["pod, school, herd, or turmoil",
         make_list(terms=terms, group="{} of porpoises")],
        ["covey",           make_list(terms=terms, group="{} of ptarmigan")],
        ["litter",          make_list(terms=terms, group="{} of pups")],
        ["bevy or drift",   make_list(terms=terms, group="{} of quail")],
        ["string",          make_list(terms=terms, group="{} of racehorses")],
        ["unkindness",      make_list(terms=terms, group="{} of ravens")],
        ["crash",           make_list(terms=terms, group="{} of rhinoceros")],
        ["bevy",            make_list(terms=terms, group="{} of roes")],
        ["parliament or building",
         make_list(terms=terms, group="{} of rooks")],
        ["hill",            make_list(terms=terms, group="{} of ruffs")],
        ["pod, herd, or rookery",
         make_list(terms=terms, group="{} of seals")],
        ["flock, herd, trip, or mob",
         make_list(terms=terms, group="{} of sheep")],
        ["dropping",        make_list(terms=terms, group="{} of sheldrake")],
        ["wisp or walk",    make_list(terms=terms, group="{} of snipe")],
        ["host",            make_list(terms=terms, group="{} of sparrows")],
        ["murmuration",     make_list(terms=terms, group="{} of starlings")],
        ["flight",          make_list(terms=terms, group="{} of swallows")],
        ["game or (if in air) a wedge",
         make_list(terms=terms, group="{} of swans")],
        ["drift, herd, or sounder",
         make_list(terms=terms, group="{} of swine")],
        ["spring",          make_list(terms=terms, group="{} of teal")],
        ["knot",            make_list(terms=terms, group="{} of toads")],
        ["hover",           make_list(terms=terms, group="{} of trout")],
        ["rafter",          make_list(terms=terms, group="{} of turkeys")],
        ["bale or turn",    make_list(terms=terms, group="{} of turtles")],
        ["bunch, knob, or raft",
         make_list(terms=terms, group="{} of waterfoul")],
        ["school, pod, herd, or gam",
         make_list(terms=terms, group="{} of whales")],
        ["company or trip", make_list(terms=terms, group="{} of wigeon")],
        ["sounder",         make_list(terms=terms, group="{} of wild boar")],
        ["destruction",     make_list(terms=terms, group="{} of wild cats")],
        ["team",
         make_list(terms=terms, group="{} of wild ducks in flight")],
        ["bunch, trip, plump, or knob (fewer than 30)",
         make_list(terms=terms, group="{} of wildfowl")],
        ["drift",           make_list(terms=terms, group="{} of wild pigs")],
        ["pack or rout",    make_list(terms=terms, group="{} of wolves")],
        ["fall",            make_list(terms=terms, group="{} of woodcock")],
        ["descent",         make_list(terms=terms, group="{} of woodpeckers")],
        ["herd",            make_list(terms=terms, group="{} of wrens")],
        ["zeal",            make_list(terms=terms, group="{} of zebras")],
        ]

    return preferred_forms_check(text, preferences, err, msg)
