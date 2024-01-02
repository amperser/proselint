"""Tests for misc.phrasal_adjectives check."""

from proselint.checks.misc import phrasal_adjectives
from tests.conftest import assert_fail, assert_pass


def test_misc():
    """Basic smoke test for misc.phrasal_adjectives."""
    check = phrasal_adjectives.check
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "There were across the board discounts.")


def test_ly():
    """Basic smoke test for misc.phrasal_adjectives.check_ly."""
    check = phrasal_adjectives.check_ly
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "He ran swiftly-fast.")
    assert_pass(check, "The not-so-hotly-contested result was fine.")
