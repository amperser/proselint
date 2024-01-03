"""Tests for terms.venery check."""

from proselint.checks.terms.venery import check
from tests.conftest import assert_fail, assert_pass


def test():
    """Basic smoke test for terms.venery."""
    assert_pass(check, "Smoke phrase with nothing flagged.")

    assert_pass(check, "There was a congregation of alligators.")
    assert_fail(check, "There was a group of alligators.")

    assert_pass(check, "There was a wisdom of wombats.")
    assert_fail(check, "There was a bunch of wombats.")
