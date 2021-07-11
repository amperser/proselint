#!/usr/bin/env python

"""Test GMEU entry 'a', part B."""


from proselint.tools import assert_error

from tests.check import Check


class chk:
    def check(self, text):
        return assert_error, text, "misc.a_distributive"


class TestCheck(Check):
    """The test class for GMEU entry A - using a over per in the distributive
    sense.
    """

    @property
    def this_check(self):
        return chk

    def test_smoke(self):
        sentences = [
            "An apple per day keeps the doctor away.",
            "I sleep eight hours per night.",
            "Their policy allows one golf cart a couple.",
            "The company donated five books a student.",
            "Our a-unit cost is less than $1000.",
            "The $50-a-parent fee seems unreasonably high."
        ]
        for sentence in sentences:
            assert not self.passes(sentence)
