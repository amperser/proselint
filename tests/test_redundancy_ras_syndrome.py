"""Tests for redundancy.ras_syndrome check."""

from proselint.checks.redundancy.ras_syndrome import check
from tests.conftest import _fail, _pass


def test_smoke():
    """Basic smoke test for redundancy.ras_syndrome."""
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _fail(check, "Please enter your PIN number.")
