"""Tests for spelling.athletes check."""

from proselint.checks.spelling.athletes import check
from tests.conftest import assert_fail
from tests.conftest import assert_pass


def test():
    """Basic smoke test for spelling.athletes."""
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "One of the greats: Cal Ripkin.")
