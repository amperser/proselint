"""Tests for misc.illogic check."""

from proselint.checks.misc import illogic

from tests.conftest import assert_fail, assert_pass


def test_misc():
    """Basic smoke test for misc.illogic."""
    check = illogic.check
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "We should preplan the trip.")


def test_coin_a_phrase_from():
    """Basic smoke test for misc.illogic.check_coin_a_phrase_from."""
    check = illogic.check_coin_a_phrase_from
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "To coin a phrase from him, No diggity")


def test_without_your_collusion():
    """Basic smoke test for misc.illogic."""
    check = illogic.check_without_your_collusion
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "Not Without your collusion you won't'.")
