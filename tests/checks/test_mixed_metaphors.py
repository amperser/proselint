"""Tests for mixed_metaphors.misc check."""

from proselint.checks.mixed_metaphors import misc
from tests.conftest import assert_fail
from tests.conftest import assert_pass


def test_bottleneck():
    """Basic smoke test for check_bottleneck."""
    check = misc.check_bottleneck
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "The project produced a huge bottleneck.")


def test_misc():
    """Basic smoke test for check_misc."""
    check = misc.check_misc
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "Writing tests is not rocket surgery.")
