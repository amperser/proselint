"""Tests for spelling.misc check."""

from proselint.checks.spelling.misc import check
from tests.conftest import assert_fail
from tests.conftest import assert_pass


def test():
    """Basic smoke test for spelling.misc."""
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "I like this alot.")
