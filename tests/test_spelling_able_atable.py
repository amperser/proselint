"""Tests for spelling.able_atable check."""

from proselint.checks.spelling.able_atable import check
from tests.conftest import _fail, _pass


def test_smoke():
    """Basic smoke test for spelling.able_atable."""
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _fail(check, "There was a demonstratable difference.")
