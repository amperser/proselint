"""Tests for consistency.spacing check."""

from proselint.checks.consistency.spacing import check
from tests.conftest import _fail, _pass


def test_smoke():
    """Basic smoke test for consistency.spacing."""
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _pass(check, "This is good. Only one space each time. Every time.")
    assert _fail(check, "This is bad.  Not consistent. At all.")
