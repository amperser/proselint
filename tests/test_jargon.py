"""Tests for jargon.misc check."""

from proselint.checks.jargon.misc import check
from tests.conftest import _pass, _fail


def test_smoke():
    """Basic smoke test for jargon.misc."""
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _fail(check, "I agree it's in the affirmative.")
