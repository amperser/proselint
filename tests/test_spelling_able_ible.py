"""Tests for spelling.able_ible check."""

from proselint.checks.spelling.able_ible import check
from tests.conftest import _pass, _fail


def test_smoke():
    """Basic smoke test for spelling.able_ible."""
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _fail(check, "It was a sensable decision.")
