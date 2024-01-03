"""Test uncomparables.misc"""

from proselint.checks.uncomparables.misc import check
from tests.conftest import assert_fail, assert_pass


def test_misc():
    """Basic smoke test for uncomparables.misc."""
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "The item was more unique.")


def test_sample_phrases():
    """Find 'very unique'."""
    assert_fail(check, "This sentence is very unique.")


def test_spaces():
    """Handle spacing correctly."""
    assert_fail(check, "This sentence is very\nunique.")
    assert_fail(check, "Kind of complete.")
    assert_pass(check, "Every perfect instance.")


def test_constitutional():
    """Don't flag exceptions."""
    assert_pass(check, "A more perfect union.")
    assert_pass(check, "A more possible future.")
    assert_fail(check, "An increasingly possible future.")
