"""Tests for misc.not_guilty check."""

from proselint.checks.misc.not_guilty import check

from .conftest import _fail, _pass


def test_smoke():
    """Basic smoke test for misc.not_guilty."""
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _fail(check, "She is not guilty beyond a reasonable doubt.")
