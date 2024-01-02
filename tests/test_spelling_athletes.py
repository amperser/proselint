"""Tests for spelling.athletes check."""

from proselint.checks.spelling.athletes import check

from .check import Check
from .conftest import _pass, _fail


def test_smoke():
    """Basic smoke test for spelling.athletes."""
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _fail(check, "One of the greats: Cal Ripkin.")
