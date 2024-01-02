"""Tests for spelling.athletes check."""

from proselint.checks.spelling.athletes import check

from .conftest import _fail, _pass


def test_smoke():
    """Basic smoke test for spelling.athletes."""
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _fail(check, "One of the greats: Cal Ripkin.")
