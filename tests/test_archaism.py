"""Tests for archaism.misc check."""

from proselint.checks.archaism.misc import check
from tests.conftest import _pass, _fail


def test_smoke():
    """Basic smoke test for archaism.misc."""
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _pass(check, "I want to sleep, and maybe dream.")
    assert _fail(check, "I want to sleep, perchance to dream.")
