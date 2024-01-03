"""Tests for cursing.nfl check."""

from proselint.checks.cursing import nfl
from tests.conftest import assert_fail, assert_pass


def test_a():
    """Basic smoke test for cursing.nfl."""
    check = nfl.check_a_to_e
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "The QB is named ball licker.")


def test_f():
    """Basic smoke test for cursing.nfl."""
    check = nfl.check_f_to_h
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "The difference between femme and famme.")


def test_i():
    """Basic smoke test for cursing.nfl."""
    check = nfl.check_i_to_p
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "Interracial is the word.")
    assert_fail(check, "you jackass, be funny.")


def test_q():
    """Basic smoke test for cursing.nfl."""
    check = nfl.check_q_to_z
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "To rent a fuck or not to rent a fuck.")
