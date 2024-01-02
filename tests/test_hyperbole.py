"""Tests for hyperbole.misc check."""

from proselint.checks.hyperbole.misc import check
from tests.conftest import assert_fail, assert_pass


def test():
    """Basic smoke test for hyperbole.misc."""
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "So exaggerated!!!")
