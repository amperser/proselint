"""Tests for spelling.ally_ly check."""

from proselint.checks.spelling.ally_ly import check

from .conftest import assert_fail, assert_pass


def test():
    """Basic smoke test for spelling.ally_ly."""
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "She was accidently fired.")
