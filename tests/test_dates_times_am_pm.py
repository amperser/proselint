"""Tests for dates_times.am_pm check."""

from proselint.checks.dates_times import am_pm
from tests.conftest import _pass, _fail


def test_smoke_check_lowercase_periods():
    """Basic smoke test.

    This is for the function
    dates_times.am_pm.check_lowercase_periods.

    """
    check = am_pm.check_lowercase_periods
    assert _pass(check, "Basic smoke phrase without issues.")
    assert _pass(check, "It happened at 7 a.m.")
    assert _fail(check, "It happened at 7 am.")
    assert _fail(check, "On Wed, Sep 21, 2016 at 11:42 AM -0400, X wrote:")


def test_smoke_check_spacing():
    """Basic smoke test.

    This is for the function
    dates_times.am_pm.check_spacing.

    """
    check = am_pm.check_spacing
    assert _pass(check, "Basic smoke phrase without issues.")
    assert _pass(check, "It happened at 7 a.m.")
    assert _fail(check, "It happened at 7a.m.")


def test_smoke_check_midnight_noon():
    """Basic smoke test.

    This for the function
    dates_times.am_pm.midnight_noon.

    """
    check = am_pm.check_midnight_noon
    assert _pass(check, "Basic smoke phrase without issues.")
    assert _pass(check, "It happened at noon.")
    assert _fail(check, "It happened at 12 a.m.")


def test_smoke_check_redundancy():
    """Basic smoke test.

    This for the function
    dates_times.am_pm.check_redundancy.

    """
    check = am_pm.check_redundancy
    assert _pass(check, "Basic smoke phrase without issues.")
    assert _pass(check, "It happened at 7 a.m.")
    assert _pass(check, "It happened at 7a.m. in the morning.")
