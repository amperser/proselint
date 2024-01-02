"""Tests for dates_times.dates check."""

from proselint.checks.dates_times import dates
from tests.conftest import _pass, _fail


def test_smoke_check_decade_apostrophes_short():
    """Basic smoke test.

    This for the function
    dates_times.dates.check_decade_apostrophes_short.

    """
    check = dates.check_decade_apostrophes_short
    assert _pass(check, "Basic smoke phrase without issues.")
    assert _pass(check, "It happened in the 90s.")
    assert _fail(check, "It happened in the 90's.")


def test_smoke_check_decade_apostrophes_long():
    """Basic smoke test.

    This is for the function
    dates_times.dates.decade_apostrophes_long.

    """
    check = dates.check_decade_apostrophes_long
    assert _pass(check, "Basic smoke phrase without issues.")
    assert _pass(check, "It happened in the 1980s.")
    assert _fail(check, "It happened in the 1980's.")

def test_smoke_check_dash_and_from():
    """Basic smoke test.

    This for the function
    dates_times.dates.dash_and_from.

    """
    check = dates.check_dash_and_from
    assert _pass(check, "Basic smoke phrase without issues.")
    assert _pass(check, "It happened from 2000 to 2005.")
    assert _fail(check, "It happened from 2000-2005.")

def test_smoke_check_month_year_comma():
    """Basic smoke test.

    This is for the function
    dates_times.dates.check_month_year_comma.

    """
    check = dates.check_month_year_comma
    assert _pass(check, "Basic smoke phrase without issues.")
    assert _pass(check, "It happened in August 2008.")
    assert _fail(check, "It happened in August, 2008.")


def test_smoke_check_month_of_year():
    """Basic smoke test.

    This is for the function
    dates_times.dates.check_month_of_year.

    """
    check = dates.check_month_of_year
    assert _pass(check, "Basic smoke phrase without issues.")
    assert _pass(check, "It happened in August 2008.")
    assert _fail(check, "It happened in August of 2008.")
