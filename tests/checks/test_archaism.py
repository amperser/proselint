"""Tests for archaism.misc check."""

from proselint.checks.archaism.misc import check
from tests.conftest import assert_fail, assert_pass


def test():
    """Basic smoke test for archaism.misc."""
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_pass(check, "I want to sleep, and maybe dream.")
    assert_fail(check, "I want to sleep, perchance to dream.")
