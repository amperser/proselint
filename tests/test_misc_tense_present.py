"""Tests for misc.tense_present check."""

from proselint.checks.misc.tense_present import check
from tests.conftest import assert_fail, assert_pass


def test():
    """Basic smoke test for misc.tense_present."""
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "I did it on accident honestly.")
