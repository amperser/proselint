"""Tests for misc.capitalization check."""

from proselint.checks.misc import capitalization
from tests.conftest import _fail, _pass


def test_smoke():
    """Basic smoke test for misc.capitalization.check."""
    check = capitalization.check
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _fail(check, "It goes back to the stone age.")


def test_smoke_check_months():
    """Basic smoke test for misc.capitalization.check_months."""
    check = capitalization.check_months
    assert _pass(check, "Smoke phrase with nothing flagged")
    assert _fail(check, "A nice day in june.")


def test_smoke_check_days():
    """Basic smoke test for misc.capitalization.check_days."""
    check = capitalization.check_days
    assert _pass(check, "Smoke phrase with nothing flagged")
    assert _fail(check, "It happened on friday.")
