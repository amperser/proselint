"""Tests for skunked_terms.misc check."""

from proselint.checks.skunked_terms.misc import check
from tests.conftest import _fail, _pass


def test_smoke():
    """Basic smoke test for skunked_terms.misc."""
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _fail(check, "I gave an impassionate defence of the situation.")
