"""Tests for spelling.able_ible check."""

from proselint.checks.spelling.able_ible import check
from tests.conftest import assert_fail
from tests.conftest import assert_pass


def test():
    """Basic smoke test for spelling.able_ible."""
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "It was a sensable decision.")
