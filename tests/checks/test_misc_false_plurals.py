"""Tests for misc.false_plurals check."""

from tests.conftest import assert_fail
from tests.conftest import assert_pass
from proselint.checks.misc import plurals

def test_misc():
    """Basic smoke test for misc.false_plurals."""
    check = plurals.check
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "There were several phenomenons.")


def test_kudos():
    """Basic smoke test for misc.false_plurals.kudos."""
    check = plurals.check_kudos
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "I give you many kudos.")
