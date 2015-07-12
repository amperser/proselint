"""Test garner.dates."""

from check import Check
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
        text = """Dr. Dre suggested to 50's manager that he look into signing
                  Eminem to the G-Unit record label."""
        errors = dates.check_decade_apostrophes_short(text)
        assert len(errors) == 0
