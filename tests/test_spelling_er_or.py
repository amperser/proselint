"""Tests for spelling.er_or check."""

from proselint.checks.spelling.er_or import check
from tests.conftest import _pass, _fail


def test_smoke():
    """Basic smoke test for spelling.er_or."""
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _fail(check, "She met with the invester.")
