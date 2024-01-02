"""Tests for misc.false_plurals check."""

from proselint.checks.misc import false_plurals

from .conftest import assert_fail, assert_pass


def test_misc():
    """Basic smoke test for misc.false_plurals."""
    check = false_plurals.check
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "There were several phenomenons.")


def test_kudos():
    """Basic smoke test for misc.false_plurals.kudos."""
    check = false_plurals.check_kudos
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "I give you many kudos.")
