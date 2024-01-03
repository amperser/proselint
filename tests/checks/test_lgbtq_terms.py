"""Tests for lgbtq.offensive_terms check."""

from proselint.checks.lgbtq.terms import check
from tests.conftest import assert_fail, assert_pass


def test_misc():
    """Basic smoke test for lgbtq.terms."""
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_pass(check, "They were a gay couple.")
    assert_fail(check, "He was a homosexual man.")


def test_homosexual_term():
    """Check that the term homosexual does not get caught."""
    assert_pass(check, "Homosexual.")


def test_sexual_preference():
    """Check that sexual preference is flagged."""
    assert_fail(check, "My sexual preference is for women.")
