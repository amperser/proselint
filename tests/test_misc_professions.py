"""Tests for misc.professions check."""

from proselint.checks.misc.professions import check

from .conftest import _fail, _pass


def test_smoke():
    """Basic smoke test for misc.professions."""
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _fail(check, "I really need a shoe repair guy.")
