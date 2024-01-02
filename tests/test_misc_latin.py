"""Tests for misc.latin check."""

from proselint.checks.misc.latin import check

from .check import Check
from .conftest import _pass, _fail


def test_smoke():
    """Basic smoke test for misc.latin."""
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _fail(check, "And ceteris paribus, it was good.")
