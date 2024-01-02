"""Tests for misc.scare_quotes check."""

from proselint.checks.misc.scare_quotes import check

from .check import Check
from .conftest import _pass, _fail


def test_smoke():
    """Basic smoke test for misc.scare_quotes."""
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _fail(check, "What was the 'take-home message'?")
