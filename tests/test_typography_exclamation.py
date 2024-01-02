"""Tests for typography.exclamation check."""

from proselint.checks.typography import exclamation
from tests.conftest import _fail, _pass


def test_smoke_repeated_exclamations():
    """Basic smoke test.

    Test for typography.exclamation.check_repeated_exclamations.
    """
    check = exclamation.check_repeated_exclamations
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _fail(check, "I'm really excited!!")


def test_smoke_exclamations_ppm():
    """Basic smoke test.

    Test for typography.exclamation.check_exclamations_ppm.
    """
    check = exclamation.check_exclamations_ppm
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _fail(check, "I'm really excited! Really!")
