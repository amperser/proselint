"""Tests for spelling.er_or check."""

from proselint.checks.spelling.er_or import check
from tests.conftest import assert_fail, assert_pass


def test():
    """Basic smoke test for spelling.er_or."""
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "She met with the invester.")
