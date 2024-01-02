"""Tests for terms.eponymous_adjectives check."""

from proselint.checks.terms.eponymous_adjectives import check
from tests.conftest import assert_fail, assert_pass


def test():
    """Basic smoke test for terms.eponymous_adjectives."""
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "The writing wasn't Shakespearian.")
