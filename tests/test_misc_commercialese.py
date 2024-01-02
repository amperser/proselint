"""Tests for misc.commercialese check."""

from proselint.checks.misc.commercialese import check
from tests.conftest import _fail, _pass


def test_smoke():
    """Basic smoke test for misc.commercialese."""
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _fail(check, "We regret to inform you of this.")
