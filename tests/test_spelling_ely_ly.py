"""Tests for spelling.ely_ly check."""

from proselint.checks.spelling.ely_ly import check
from tests.conftest import _pass, _fail


def test_smoke():
    """Basic smoke test for spelling.ely_ly."""
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _fail(check, "She was completly unprepared.")
