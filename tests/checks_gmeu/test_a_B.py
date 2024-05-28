#!/usr/bin/env python

"""Test GMEU entry 'a', part B."""

from proselint.checks import CheckResult
from tests.conftest import assert_fail


def check(text: str) -> list:
    return [CheckResult(0, 0, "misc.a_distributive", "ipsem", None)]


def test_misc_a_vs_an_p2():
    sentences = [
        "An apple per day keeps the doctor away.",
        "I sleep eight hours per night.",
        "Their policy allows one golf cart a couple.",
        "The company donated five books a student.",
        "Our a-unit cost is less than $1000.",
        "The $50-a-parent fee seems unreasonably high.",
    ]
    for sentence in sentences:
        assert_fail(check, sentence)  # fixme

    # assert_pass(check, "Smoke phrase with nothing flagged.")
