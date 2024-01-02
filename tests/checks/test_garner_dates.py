"""Test garner.dates."""
from proselint.checks.dates_times import dates
from tests.conftest import assert_fail, assert_pass


def test_50s_hyphenation():
    """Find unneeded hyphen in 50's."""

    text = """The 50's were swell."""
    check = dates.check_decade_apostrophes_short
    assert_fail(check, text)


def test_50_cent_hyphenation():
    """Don't flag 50's when it refers to 50 Cent's manager."""
    text = """
        Dr. Dre suggested to 50's manager that he look into signing
        Eminem to the G-Unit record label.
    """
    check = dates.check_decade_apostrophes_short
    assert_pass(check, text)


def test_dash_and_from():
    """Test garner.check_dash_and_from."""
    text = """From 1999-2002, Sally served as chair of the committee."""
    check = dates.check_dash_and_from
    assert_fail(check, text)
