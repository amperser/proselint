"""Tests for terms.eponymous_adjectives check."""

from proselint.checks.terms.eponymous_adjectives import check
from tests.conftest import _pass, _fail


def test_smoke():
    """Basic smoke test for terms.eponymous_adjectives."""
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _fail(check, "The writing wasn't Shakespearian.")
