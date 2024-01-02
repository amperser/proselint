"""Tests for lgbtq.offensive_terms check."""

from proselint.checks.lgbtq.terms import check

from .check import Check
from .conftest import _pass, _fail


def test_smoke():
    """Basic smoke test for lgbtq.terms."""
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _pass(check, "They were a gay couple.")
    assert _fail(check, "He was a homosexual man.")

def test_homosexual_term():
    """Check that the term homosexual does not get caught."""
    assert _pass(check, "Homosexual.")

def test_sexual_prefence():
    """Check that sexual preference is flagged."""
    assert _fail(check, "My sexual preference is for women.")
