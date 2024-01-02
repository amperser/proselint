"""Tests for misc.professions check."""

from proselint.checks.misc.professions import check

from tests.conftest import assert_fail, assert_pass


def test():
    """Basic smoke test for misc.professions."""
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "I really need a shoe repair guy.")
