"""Tests for sexism.misc check."""

from proselint.checks.sexism.misc import check

from .check import Check
from .conftest import _pass, _fail


def test_smoke():
    """Basic smoke test for sexism.misc."""
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _fail(check, "The legal team had two lawyers and a lady lawyer.")
