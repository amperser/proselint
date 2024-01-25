"""Tests for spelling.ance_ence check."""

from proselint.checks.spelling.ance_ence import check
from tests.conftest import assert_fail
from tests.conftest import assert_pass


def test():
    """Basic smoke test for spelling.ance_ence."""
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "The resistence was futile.")
