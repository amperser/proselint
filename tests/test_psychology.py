"""Tests for psychology.misc check."""

from proselint.checks.psychology import misc
from tests.conftest import _fail, _pass


def test_smoke_lie_detector_test():
    """Basic smoke test for psychology.misc.check_lie_detector_test."""
    check = misc.check_lie_detector_test
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _fail(check, "The defendant took a lie detector test.")


def test_smoke_p_equals_zero():
    """Basic smoke test for psychology.misc.check_p_equals_zero."""
    check = misc.check_p_equals_zero
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _fail(check, "The effect was highly signficant at p = 0.00.")


def test_smoke_mental_telepathy():
    """Basic smoke test for psychology.misc.check_mental_telepathy."""
    check = misc.check_mental_telepathy
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _fail(check, "I've been practicing mental telepathy.")
