"""Tests for spelling.misc check."""

from proselint.checks.spelling.misc import check
from tests.conftest import _fail, _pass


def test_smoke():
    """Basic smoke test for spelling.misc."""
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _fail(check, "I like this alot.")
