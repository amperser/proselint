"""Test garner.dates."""
from __future__ import absolute_import
from __future__ import print_function

from .check import Check
from proselint.checks.garner import dates


class TestCheck(Check):

    """Test class for garner.dates."""

    __test__ = True

    def test_50s_hyphenation(self):
        """Find uneeded hyphen in 50's."""
        text = """The 50's were swell."""
        errors = dates.check_decade_apostrophes_short(text)
        assert len(errors) == 1

    def test_50_Cent_hyphenation(self):
        """Don't flag 50's when it refers to 50 Cent's manager."""
        text = """
            Dr. Dre suggested to 50's manager that he look into signing
            Eminem to the G-Unit record label.
        """
        errors = dates.check_decade_apostrophes_short(text)
        assert len(errors) == 0

    def test_dash_and_from(self):
        """Test garner.check_dash_and_from."""
        text = """From 1999-2002, Sally served as chair of the committee."""
        errors = dates.check_dash_and_from(text)
        print(errors)
        assert len(errors) == 1
