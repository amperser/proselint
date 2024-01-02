"""Tests for misc.suddenly check."""

from proselint.checks.misc.suddenly import check

from .conftest import _fail, _pass


def test_smoke():
    """Basic smoke test for misc.suddenly."""
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _fail(check, "Suddenly, it all made sense.")
