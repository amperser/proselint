"""Tests for spelling.in_un check."""

from proselint.checks.spelling.in_un import check
from tests.conftest import assert_fail
from tests.conftest import assert_pass


def test():
    """Basic smoke test for spelling.in_un."""
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "The plan was unfeasible.")
