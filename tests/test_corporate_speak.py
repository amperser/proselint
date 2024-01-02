"""Tests for corporate_speak.misc check."""

from proselint.checks.corporate_speak.misc import check

from .check import Check
from .conftest import _pass, _fail


def test_smoke():
    """Basic smoke test for corporate_speak.misc."""
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _pass(check, "We will discuss it later.")
    assert _fail(check, "We will circle back around to it.")
