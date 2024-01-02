"""Tests for weasel_words.very check."""

from proselint.checks.weasel_words.very import check
from tests.conftest import _fail, _pass


def test_smoke():
    """Basic smoke test for weasel_words.very."""
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _fail(check, "The book was very interesting.")
