"""Tests for weasel_words.very check."""

from proselint.checks.weasel_words.very import check
from tests.conftest import assert_fail, assert_pass


def test():
    """Basic smoke test for weasel_words.very."""
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "The book was very interesting.")
