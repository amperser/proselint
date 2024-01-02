"""Tests for misc.debased check."""

from proselint.checks.misc.debased import check

from .check import Check
from .conftest import _pass, _fail


def test_smoke():
    """Basic smoke test for misc.debased."""
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _fail(check, "This leaves much to be desired.")
