"""Tests for lgbtq.terms check."""

from proselint.checks.lgbtq.offensive_terms import check
from tests.conftest import _pass, _fail


def test_smoke():
    """Basic smoke test for lgbtq.offensive_terms."""
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _pass(check, "I once met a gay man.")
    assert _fail(check, "I once met a fag.")
