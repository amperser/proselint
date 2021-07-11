#!/usr/bin/env python

"""Test GMEU entry 'a', part A."""


from proselint.tools import assert_error

from tests.check import Check


class chk:
    def check(self, text):
        return assert_error, text, "misc.a_vs_an"


class TestCheck(Check):
    """The test class for GMEU entry A - using the correct determiner."""

    @property
    def this_check(self):
        return chk

    sentences_with_errors = [
        "Are you an Yankee fan?",
        "Coffee tastes less sweet in an white mug.",
        "One of them wore a opalescent vest.",
        "You're a intelligent guy, often misguided.",
        "Ezra gave an eulogy.",
        "What capital of an European country is the farthest north?",
        "His sole reward was an one-year term as Ambassador to Thailand.",
        "I will be relying on a roulette wheel and an Ouija board.",
        "Anyone in an uniform is fair game.",
        "Grimm started working as a F.B.I. agent in 1995.",
        "Out of 186 managers participating, 57 had a MBA degree.",
        "Smith announced that a SEC filing is pending.",
        "This argument is an historical desecration.",
        "The treatment of crime in Britain shows an historic shift away…",
        "It is, in some ways, an humble form.",
        "The thief turned out to be an habitual offender from Darlington.",
        "This stage displays an hallucinatory image that signifies itself.",
        "He saw an hallucinatory image before passing out.",
        "A triumphant Adolf Hitler addressed an hysterical crowd.",
        "Kun pieced together an history of gender-segregated dining in L.A.",
        "An historian who fled the Nazis and still wants us to read Hitler.",
        "It is nominally an historical novel.",
        "It feels good to validate an hypothesis.",
        "An hereditary title can be passed to a member of the family.",
        "The Clinton Presidency was an historic era of prosperity.",
        "There comes to be an habitual pattern between neurons in the brain.",
        "They had the authority to start an humanitarian intervention.",
        "She laughed aloud, an hysterical sort of giggled, quickly stifled",
    ]

    def test_smoke(self):
        for sentence in self.sentences_with_errors:
            assert not self.passes(sentence)
