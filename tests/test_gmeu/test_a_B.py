#!/usr/bin/env python

"""Test GMEU entry 'a', part B."""

from tests.check import assert_error
from tests.conftest import _fail


class Chk:
    def check(self, text):
        return assert_error, text, "misc.a_distributive"


def test_smoke():
    sentences = [
        "An apple per day keeps the doctor away.",
        "I sleep eight hours per night.",
        "Their policy allows one golf cart a couple.",
        "The company donated five books a student.",
        "Our a-unit cost is less than $1000.",
        "The $50-a-parent fee seems unreasonably high.",
    ]
    for sentence in sentences:
        assert _fail(check, sentence)  #fixme
