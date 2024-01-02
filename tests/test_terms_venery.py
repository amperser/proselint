"""Tests for terms.venery check."""

from proselint.checks.terms.venery import check
from tests.conftest import assert_fail, assert_pass


def test():
    """Basic smoke test for terms.venery."""
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "There was a group of alligators.")
