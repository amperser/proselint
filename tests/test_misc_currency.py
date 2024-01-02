"""Tests for misc.currency check."""

from proselint.checks.misc.currency import check

from .check import Check
from .conftest import _pass, _fail


def test_smoke():
    """Basic smoke test for misc.currency."""
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _fail(check, "It cost $10 dollars.")
