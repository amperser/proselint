"""Tests for redundancy.misc check."""

from proselint.checks.redundancy import misc
from tests.conftest import assert_fail, assert_pass


def test_misc():
    """Basic smoke test for redundancy.misc.check."""
    check = misc.check
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "The table was rectangular in shape.")


def test_garner():
    """Basic smoke test for redundancy.misc.check_garner."""
    check = misc.check_garner
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "It was blatantly obvious what to do next.")


def test_nordquist():
    """Basic smoke test for redundancy.misc.check_norquist."""
    check = misc.check_nordquist
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "Taking the package was absolutely essential.")


def test_atd():
    """Basic smoke test for redundancy.misc.check_norquist."""
    check = misc.check_atd
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "He often repeated the old adage.")
