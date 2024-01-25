"""Tests for redundancy.ras_syndrome check."""

from proselint.checks.redundancy.ras_syndrome import check
from tests.conftest import assert_fail
from tests.conftest import assert_pass


def test():
    """Basic smoke test for redundancy.ras_syndrome."""
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "Please enter your PIN number.")
