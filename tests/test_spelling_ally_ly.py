"""Tests for spelling.ally_ly check."""

from proselint.checks.spelling.ally_ly import check

from .check import Check
from .conftest import _pass, _fail


def test_smoke():
    """Basic smoke test for spelling.ally_ly."""
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _fail(check, "She was accidently fired.")
