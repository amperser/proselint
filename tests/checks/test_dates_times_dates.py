"""Tests for dates_times.dates check."""

from proselint.checks.dates_times import dates
from tests.conftest import assert_fail
from tests.conftest import assert_pass


def test_decade_apostrophes_short():
    """Basic smoke test.

    This for the function
    dates_times.dates.check_decade_apostrophes_short.

    """
    check = dates.check_decade_apostrophes_short
    assert_pass(check, "Basic smoke phrase without issues.")
    assert_pass(check, "It happened in the 90s.")
    assert_fail(check, "It happened in the 90's.")


def test_decade_apostrophes_long():
    """Basic smoke test.

    This is for the function
    dates_times.dates.decade_apostrophes_long.

    """
    check = dates.check_decade_apostrophes_long
    assert_pass(check, "Basic smoke phrase without issues.")
    assert_pass(check, "It happened in the 1980s.")
    assert_fail(check, "It happened in the 1980's.")


def test_dash_and_from():
    """Basic smoke test.

    This for the function
    dates_times.dates.dash_and_from.

    """
    check = dates.check_dash_and_from
    assert_pass(check, "Basic smoke phrase without issues.")
    assert_pass(check, "It happened from 2000 to 2005.")
    assert_fail(check, "It happened from 2000-2005.")


def test_month_year_comma():
    """Basic smoke test.

    This is for the function
    dates_times.dates.check_month_year_comma.

    """
    check = dates.check_month_year_comma
    assert_pass(check, "Basic smoke phrase without issues.")
    assert_pass(check, "It happened in August 2008.")
    assert_fail(check, "It happened in August, 2008.")


def test_month_of_year():
    """Basic smoke test.

    This is for the function
    dates_times.dates.check_month_of_year.

    """
    check = dates.check_month_of_year
    assert_pass(check, "Basic smoke phrase without issues.")
    assert_pass(check, "It happened in August 2008.")
    assert_fail(check, "It happened in August of 2008.")
