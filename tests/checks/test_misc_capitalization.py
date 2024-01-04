"""Tests for misc.capitalization check."""

from proselint.checks.misc import capitalization
from tests.conftest import assert_fail
from tests.conftest import assert_pass


def test_misc():
    """Basic smoke test for misc.capitalization.check."""
    check = capitalization.check
    assert_pass(check, "Smoke Stone Age with nothing flagged.")
    assert_fail(check, "It goes back to the stone age.")


def test_seasons():
    """Basic smoke test for misc.capitalization.check_months."""
    check = capitalization.check_seasons
    assert_pass(check, "Smoke winter with nothing flagged")
    assert_fail(check, "A nice day during Winter.")
    assert_fail(check, "A nice day in Spring.")


def test_months():
    """Basic smoke test for misc.capitalization.check_months."""
    check = capitalization.check_months
    assert_pass(check, "Smoke phrase with nothing flagged")
    assert_fail(check, "A nice day in june.")


def test_days():
    """Basic smoke test for misc.capitalization.check_days."""
    check = capitalization.check_days
    assert_pass(check, "Smoke phrase with nothing flagged")
    assert_fail(check, "It happened on friday.")
