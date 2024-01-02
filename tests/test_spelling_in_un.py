"""Tests for spelling.in_un check."""

from proselint.checks.spelling.in_un import check
from tests.conftest import _pass, _fail


def test_smoke():
    """Basic smoke test for spelling.in_un."""
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _fail(check, "The plan was unfeasible.")
