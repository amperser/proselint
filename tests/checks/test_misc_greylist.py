"""Tests for misc.greylist check."""

from proselint.checks.misc.greylist import check
from tests.conftest import assert_fail, assert_pass


def test_misc():
    """Basic smoke test for misc.greylist."""
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "She should utilize her knowledge.")
    assert_fail(check, "This is obviously an inadvisable word to use obviously.")


def test_utilized():
    """Don't produce an error when 'use' is used correctly."""
    assert_pass(check, "I use a hammer to drive nails into wood.")
    assert_fail(check, "I utilize a hammer to drive nails into wood.")
    assert_fail(check, "Do you know anyone who *needs* to utilize the word utilize?")
