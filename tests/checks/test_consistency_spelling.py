"""Tests for consistency.spelling check."""

from proselint.checks.consistency.spelling import check
from tests.conftest import assert_fail, assert_pass


def test():
    """Basic smoke test for consistency.spelling."""
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_pass(check, "The centre for the arts is the art centre.")
    assert_pass(check, "The center for the arts is the art center.")
    assert_fail(check, "The centre of the arts is the art center.")
