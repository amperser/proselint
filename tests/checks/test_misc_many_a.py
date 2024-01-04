"""Tests for misc.many_a check."""

from proselint.checks.misc.many_a import check
from tests.conftest import assert_fail
from tests.conftest import assert_pass


def test():
    """Basic smoke test for misc.many_a."""
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "There were many a day I thought about it.")
