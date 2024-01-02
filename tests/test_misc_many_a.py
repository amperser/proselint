"""Tests for misc.many_a check."""

from proselint.checks.misc.many_a import check

from .conftest import _fail, _pass


def test_smoke():
    """Basic smoke test for misc.many_a."""
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _fail(check, "There were many a day I thought about it.")
