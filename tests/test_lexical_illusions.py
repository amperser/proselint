"""Tests for lexical_illusions.misc check."""

from proselint.checks.lexical_illusions.misc import check
from tests.conftest import _pass, _fail


def test_smoke():
    """Basic smoke test for lexical_illusions.misc."""
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _fail(check, "Paris in the the springtime.")
    assert _pass(check, "And he's gone, gone with the breeze")
    assert _pass(check, "You should know that that sentence wasn't wrong.")
    assert _pass(check, "She had had dessert on the balcony.")
    assert _fail(check, "You should know that that that was wrong.")
    assert _pass(check, "The practitioner's side")
    assert _pass(check, "An antimatter particle")
    assert _pass(check, "The theory")
    assert _pass(check, "She had coffee at the Foo-bar bar.")
