"""Tests for typography.diacritical_marks check."""

from proselint.checks.typography.diacritical_marks import check
from tests.conftest import _pass, _fail


def test_smoke():
    """Basic smoke test for typography.diacritical_marks."""
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _fail(check, "He saw the performance by Beyonce.")
