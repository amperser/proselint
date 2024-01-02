"""Tests for spelling.ance_ence check."""

from proselint.checks.spelling.ance_ence import check

from .check import Check
from .conftest import _pass, _fail


def test_smoke():
    """Basic smoke test for spelling.ance_ence."""
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _fail(check, "The resistence was futile.")
