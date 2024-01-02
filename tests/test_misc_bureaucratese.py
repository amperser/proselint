"""Tests for misc.bureaucratese check."""

from proselint.checks.misc.bureaucratese import check

from .check import Check
from .conftest import _pass, _fail


def test_smoke():
    """Basic smoke test for misc.bureaucratese."""
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _fail(check, "I hope the report meets with your approval.")
