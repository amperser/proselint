"""Tests for consistency.spacing check."""

from proselint.checks.consistency.spacing import check
from tests.conftest import assert_fail
from tests.conftest import assert_pass


def test():
    """Basic smoke test for consistency.spacing."""
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_pass(check, "This is good. Only one space each time. Every time.")
    assert_fail(check, "This is bad.  Not consistent. At all.")
