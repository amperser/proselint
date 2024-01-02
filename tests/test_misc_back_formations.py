"""Tests for misc.back_formations check."""

from proselint.checks.misc.back_formations import check
from tests.conftest import _pass, _fail


def test_smoke():
    """Basic smoke test for misc.back_formations."""
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _fail(check, "It is an improprietous use.")
