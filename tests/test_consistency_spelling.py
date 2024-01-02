"""Tests for consistency.spelling check."""

from proselint.checks.consistency.spelling import check
from tests.conftest import _pass, _fail


def test_smoke():
    """Basic smoke test for consistency.spelling."""
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _pass(check, "The centre for the arts is the art centre.")
    assert _pass(check, "The center for the arts is the art center.")
    assert _fail(check, "The centre of the arts is the art center.")
