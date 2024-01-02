"""Tests for misc.illogic check."""

from proselint.checks.misc import illogic

from .check import Check
from .conftest import _pass, _fail


def test_smoke():
    """Basic smoke test for misc.illogic."""
    check = illogic.check
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _fail(check, "We should preplan the trip.")


def test_smoke_coin_a_phrase_from():
    """Basic smoke test for misc.illogic.check_coin_a_phrase_from."""
    check = illogic.check_coin_a_phrase_from
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _fail(check, "To coin a phrase from him, No diggity")


def test_smoke_check_without_your_collusion():
    """Basic smoke test for misc.illogic."""
    check = illogic.check_without_your_collusion
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _fail(check, "Not Without your collusion you won't'.")
