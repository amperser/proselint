"""Tests for hyperbole.misc check."""

from proselint.checks.hyperbole.misc import check
from tests.conftest import _pass, _fail


def test_smoke():
    """Basic smoke test for hyperbole.misc."""
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _fail(check, "So exaggerated!!!")
