"""Tests for misc.false_plurals check."""

from proselint.checks.misc import false_plurals

from .check import Check
from .conftest import _pass, _fail


def test_smoke():
    """Basic smoke test for misc.false_plurals."""
    check = false_plurals.check
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _fail(check, "There were several phenomenons.")


def test_smoke_kudos():
    """Basic smoke test for misc.false_plurals.kudos."""
    check = false_plurals.check_kudos
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _fail(check, "I give you many kudos.")
