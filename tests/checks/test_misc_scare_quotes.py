"""Tests for misc.scare_quotes check."""

from proselint.checks.misc.scare_quotes import check
from tests.conftest import assert_fail
from tests.conftest import assert_pass


def test():
    """Basic smoke test for misc.scare_quotes."""
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "What was the 'take-home message'?")
