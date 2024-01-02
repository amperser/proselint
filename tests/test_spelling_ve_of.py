"""Tests for spelling.ve_of check."""

from proselint.checks.spelling.ve_of import check
from tests.conftest import _pass, _fail


def test_smoke():
    """Basic smoke test for spelling.ve_of."""
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _fail(check, "This could of been the third test.")
