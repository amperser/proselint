"""Tests for misc.punctuation check."""

from proselint.checks.misc.punctuation import check
from tests.conftest import _fail, _pass


def test_smoke():
    """Basic smoke test for misc.punctuation."""
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _fail(check, "See Smith et. al.")
