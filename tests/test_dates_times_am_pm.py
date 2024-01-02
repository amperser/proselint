"""Tests for dates_times.am_pm check."""

from proselint.checks.dates_times import am_pm
from tests.conftest import assert_fail, assert_pass


def test_lowercase_periods():
    """Basic smoke test.

    This is for the function
    dates_times.am_pm.check_lowercase_periods.

    """
    check = am_pm.check_lowercase_periods
    assert_pass(check, "Basic smoke phrase without issues.")
    assert_pass(check, "It happened at 7 a.m.")
    assert_fail(check, "It happened at 7 am.")
    assert_fail(check, "On Wed, Sep 21, 2016 at 11:42 AM -0400, X wrote:")


def test_spacing():
    """Basic smoke test.

    This is for the function
    dates_times.am_pm.check_spacing.

    """
    check = am_pm.check_spacing
    assert_pass(check, "Basic smoke phrase without issues.")
    assert_pass(check, "It happened at 7 a.m.")
    assert_fail(check, "It happened at 7a.m.")


def test_midnight_noon():
    """Basic smoke test.

    This for the function
    dates_times.am_pm.midnight_noon.

    """
    check = am_pm.check_midnight_noon
    assert_pass(check, "Basic smoke phrase without issues.")
    assert_pass(check, "It happened at noon.")
    assert_fail(check, "It happened at 12 a.m.")


def test_redundancy():
    """Basic smoke test.

    This for the function
    dates_times.am_pm.check_redundancy.

    """
    check = am_pm.check_redundancy
    assert_pass(check, "Basic smoke phrase without issues.")
    assert_pass(check, "It happened at 7 a.m.")
    assert_pass(check, "It happened at 7a.m. in the morning.")
