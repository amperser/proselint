"""Tests for typography.diacritical_marks check."""

from proselint.checks.typography.diacritical_marks import check
from tests.conftest import assert_fail, assert_pass


def test():
    """Basic smoke test for typography.diacritical_marks."""
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "He saw the performance by Beyonce.")
