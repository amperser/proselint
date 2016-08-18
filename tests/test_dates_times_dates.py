"""Tests for dates_times.dates check."""
from __future__ import absolute_import

from .check import Check

from proselint.checks.dates_times import dates as chk


class TestCheck(Check):
    """The test class for dates_times.dates."""

    __test__ = True

    @property
    def this_check(self):
        """Bolierplate."""
        return chk

    def test_smoke_check_decade_apostrophes_short(self):
        """Basic smoke test.

        This for the function
        dates_times.dates.check_decade_apostrophes_short.

        """
        assert chk.check_decade_apostrophes_short(
            "Basic smoke phrase without issues.") == []
        assert chk.check_decade_apostrophes_short(
            "It happened in the 90s.") == []
        assert chk.check_decade_apostrophes_short(
            "It happened in the 90's.") != []

    def test_smoke_check_decade_apostrophes_long(self):
        """Basic smoke test.

        This is for the function
        dates_times.dates.decade_apostrophes_long.

        """
        assert chk.check_decade_apostrophes_long(
            "Basic smoke phrase without issues.") == []
        assert chk.check_decade_apostrophes_long(
            "It happened in the 1980s.") == []
        assert chk.check_decade_apostrophes_long(
            "It happened in the 1980's.") != []

    def test_smoke_check_dash_and_from(self):
        """Basic smoke test.

        This for the function
        dates_times.dates.dash_and_from.

        """
        assert chk.check_dash_and_from(
            "Basic smoke phrase without issues.") == []
        assert chk.check_dash_and_from(
            "It happened from 2000 to 2005.") == []
        assert chk.check_dash_and_from(
            "It happened from 2000-2005.") != []

    def test_smoke_check_month_year_comma(self):
        """Basic smoke test.

        This is for the function
        dates_times.dates.check_month_year_comma.

        """
        assert chk.check_month_year_comma(
            "Basic smoke phrase without issues.") == []
        assert chk.check_month_year_comma(
            "It happened in August 2008.") == []
        assert chk.check_month_year_comma(
            "It happened in August, 2008.") != []

    def test_smoke_check_month_of_year(self):
        """Basic smoke test.

        This is for the function
        dates_times.dates.check_month_of_year.

        """
        assert chk.check_month_of_year(
            "Basic smoke phrase without issues.") == []
        assert chk.check_month_of_year(
            "It happened in August 2008.") == []
        assert chk.check_month_of_year(
            "It happened in August of 2008.") != []
