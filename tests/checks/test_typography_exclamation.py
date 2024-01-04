"""Tests for typography.exclamation check."""

from proselint.checks.typography import exclamation
from tests.conftest import assert_fail
from tests.conftest import assert_pass


def test_repeated_exclamations():
    """Basic smoke test.

    Test for typography.exclamation.check_repeated_exclamations.
    """
    check = exclamation.check_repeated_exclamations
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "I'm really excited!!")


def test_exclamations_ppm():
    """Basic smoke test.

    Test for typography.exclamation.check_exclamations_ppm.
    """
    check = exclamation.check_exclamations_ppm
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "I'm really excited! Really!")
