"""Tests for sexism.misc check."""

from proselint.checks.sexism.misc import check

from tests.conftest import assert_fail, assert_pass


def test():
    """Basic smoke test for sexism.misc."""
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "The legal team had two lawyers and a lady lawyer.")
