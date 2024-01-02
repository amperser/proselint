"""Tests for misc.inferior_superior check."""

from proselint.checks.misc.inferior_superior import check

from tests.conftest import assert_fail, assert_pass


def test():
    """Basic smoke test for misc.inferior_superior."""
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "It was more inferior than the alternative.")
