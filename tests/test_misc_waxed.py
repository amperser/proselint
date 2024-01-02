"""Tests for misc.waxed check."""

from proselint.checks.misc.waxed import check
from tests.conftest import _pass, _fail


def test_smoke():
    """Basic smoke test for misc.waxed."""
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _fail(check, "They really could wax poetically.")
