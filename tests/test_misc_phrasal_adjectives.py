"""Tests for misc.phrasal_adjectives check."""

from proselint.checks.misc import phrasal_adjectives

from .conftest import _fail, _pass


def test_smoke():
    """Basic smoke test for misc.phrasal_adjectives."""
    check = phrasal_adjectives.check
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _fail(check, "There were across the board discounts.")


def test_smoke_ly():
    """Basic smoke test for misc.phrasal_adjectives.check_ly."""
    check = phrasal_adjectives.check_ly
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _fail(check, "He ran swiftly-fast.")
    assert _pass(check, "The not-so-hotly-contested result was fine.")
