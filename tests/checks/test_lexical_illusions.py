"""Tests for lexical_illusions.misc check."""

from proselint.checks.lexical_illusions.misc import check
from tests.conftest import assert_fail
from tests.conftest import assert_pass


def test():
    """Basic smoke test for lexical_illusions.misc."""
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "Paris in the the springtime.")
    assert_pass(check, "And he's gone, gone with the breeze")
    assert_pass(check, "You should know that that sentence wasn't wrong.")
    assert_pass(check, "She had had dessert on the balcony.")
    assert_fail(check, "You should know that that that was wrong.")
    assert_pass(check, "The practitioner's side")
    assert_pass(check, "An antimatter particle")
    assert_pass(check, "The theory")
    assert_pass(check, "She had coffee at the Foo-bar bar.")
    assert_fail(check, "She had coffee at the Foo bar bar.")
    assert_fail(check, "She she coffee at the Foo-bar.")
