"""Tests for sexism.misc check."""

from proselint.checks.sexism import misc
from tests.conftest import assert_fail, assert_pass


def test_sexism():
    """Basic smoke test for sexism.misc."""
    check = misc.check_sexism
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "The legal team had two lawyers and a lady lawyer.")


def test_preferred_form():
    """Basic smoke test for sexism.misc."""
    check = misc.check_preferred_form
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_pass(check, "Hello Mr. Birdperson. You look good.")
    assert_pass(check, "Hello Mr. birdperson. still looking good.")
    assert_pass(check, "Oh Chairperson - happy face.")
    assert_fail(check, "Oh chairperson - why so sad.")
    assert_fail(check, "You get the mailperson.")
