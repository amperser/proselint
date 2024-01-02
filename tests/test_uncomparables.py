"""Test uncomparables.misc"""

from proselint.checks.uncomparables.misc import check
from tests.conftest import _pass, _fail


def test_smoke():
    """Basic smoke test for uncomparables.misc."""
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _fail(check, "The item was more unique.")


def test_sample_phrases():
    """Find 'very unique'."""
    assert _fail(check, "This sentence is very unique.")


def test_spaces():
    """Handle spacing correctly."""
    assert _fail(check, "This sentence is very\nunique.")
    assert _fail(check, "Kind of complete.")
    assert _pass(check, "Every perfect instance.")


def test_constitutional():
    """Don't flag exceptions."""
    assert _pass(check, "A more perfect union.")
