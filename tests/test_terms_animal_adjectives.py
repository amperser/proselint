"""Tests for terms.animal_adjectives check."""

from proselint.checks.terms.animal_adjectives import check
from tests.conftest import assert_fail, assert_pass


def test():
    """Basic smoke test for terms.animal_adjectives."""
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "It was some bird-like creature.")
