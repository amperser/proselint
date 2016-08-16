"""Tests for dates_times.am_pm check."""
from __future__ import absolute_import

from .check import Check

from proselint.checks.dates_times import am_pm as chk


class TestCheck(Check):
    """The test class for dates_times.am_pm."""

    __test__ = True

    @property
    def this_check(self):
        """Bolierplate."""
        return chk

    def test_smoke_check_lowercase_periods(self):
        """Basic smoke test.

        This is for the function
        dates_times.am_pm.check_lowercase_periods.

        """
        assert chk.check_lowercase_periods(
            "Basic smoke phrase without issues.") == []
        assert chk.check_lowercase_periods(
            "It happened at 7 a.m.") == []
        assert chk.check_lowercase_periods(
            "It happened at 7 am.") != []

    def test_smoke_check_spacing(self):
        """Basic smoke test.

        This is for the function
        dates_times.am_pm.check_spacing.

        """
        assert chk.check_spacing(
            "Basic smoke phrase without issues.") == []
        assert chk.check_spacing(
            "It happened at 7 a.m.") == []
        assert chk.check_spacing(
            "It happened at 7a.m.") != []

    def test_smoke_check_midnight_noon(self):
        """Basic smoke test.

        This for the function
        dates_times.am_pm.midnight_noon.

        """
        assert chk.check_midnight_noon(
            "Basic smoke phrase without issues.") == []
        assert chk.check_midnight_noon(
            "It happened at noon.") == []
        assert chk.check_midnight_noon(
            "It happened at 12 a.m.") != []

    def test_smoke_check_redundancy(self):
        """Basic smoke test.

        This for the function
        dates_times.am_pm.check_redundancy.

        """
        assert chk.check_redundancy(
            "Basic smoke phrase without issues.") == []
        assert chk.check_redundancy(
            "It happened at 7 a.m.") == []
        assert chk.check_redundancy(
            "It happened at 7a.m. in the morning.") != []
