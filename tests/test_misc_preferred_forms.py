"""Tests for misc.preferred_forms check."""

from proselint.checks.misc.preferred_forms import check
from tests.conftest import _fail, _pass


def test_smoke():
    """Basic smoke test for misc.preferred_forms."""
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _fail(check, "It was almost haloween.")
