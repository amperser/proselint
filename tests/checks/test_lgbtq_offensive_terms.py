"""Tests for lgbtq.terms check."""

from proselint.checks.lgbtq.offensive_terms import check
from tests.conftest import assert_fail, assert_pass


def test():
    """Basic smoke test for lgbtq.offensive_terms."""
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_pass(check, "I once met a gay man.")
    assert_fail(check, "I once met a fag.")
