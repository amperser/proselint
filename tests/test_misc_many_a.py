"""Tests for misc.many_a check."""

from proselint.checks.misc.many_a import check

from .check import Check
from .conftest import _pass, _fail


def test_smoke():
    """Basic smoke test for misc.many_a."""
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _fail(check, "There were many a day I thought about it.")
