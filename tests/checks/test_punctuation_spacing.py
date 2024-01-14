"""Tests for punctuation check."""

from proselint.checks.punctuation import spacing
from tests.conftest import assert_fail
from tests.conftest import assert_pass


def test_end_punctuation():
    """Tests end punctuation spacing."""
    check = spacing.check_end_punctuation_spacing
    assert_pass(check, "Smoke phrase with nothing flagged!")
    assert_fail(check, "flagged!    ")
    assert_pass(check, "flagged?  ")
    assert_fail(check, "flagged?    ")


def test_general_punctuation():
    """Tests general puncutation spacing."""
    check = spacing.check_general_spacing
    assert_pass(check, "The quick brown fox jumps; over the lazy dog!")
    assert_fail(check, "The quick brown fox jumps;  over the lazy dog!")
    assert_pass(check, "The quick brown fox jumps:over the lazy dog!")
    assert_pass(check, "The quick brown fox jumps  :over the lazy dog!")
