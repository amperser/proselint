"""Tests for psychology.misc check."""

from proselint.checks.psychology import misc
from tests.conftest import assert_fail
from tests.conftest import assert_pass


def test_lie_detector_test():
    """Basic smoke test for psychology.misc.check_lie_detector_test."""
    check = misc.check_lie_detector_test
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "The defendant took a lie detector test.")


def test_p_equals_zero():
    """Basic smoke test for psychology.misc.check_p_equals_zero."""
    check = misc.check_p_equals_zero
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "The effect was highly signficant at p = 0.00.")


def test_mental_telepathy():
    """Basic smoke test for psychology.misc.check_mental_telepathy."""
    check = misc.check_mental_telepathy
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "I've been practicing mental telepathy.")
