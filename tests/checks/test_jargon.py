"""Tests for jargon.misc check."""

from proselint.checks.jargon.misc import check
from tests.conftest import assert_fail
from tests.conftest import assert_pass


def test():
    """Basic smoke test for jargon.misc."""
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "I agree it's in the affirmative.")
