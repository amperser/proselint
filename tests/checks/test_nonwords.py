"""Tests for nonwords.misc check."""

from proselint.checks.nonwords.misc import check
from tests.conftest import assert_fail
from tests.conftest import assert_pass


def test():
    """Basic smoke test for nonwords.misc."""
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "The test was good irregardless.")
