"""Test garner.dates."""

from proselint.checks.dates_times import dates

from .check import Check


class TestCheck(Check):
    """Test class for garner.dates."""

    __test__ = True

    def test_50s_hyphenation(self):
        """Find unneeded hyphen in 50's."""
        text = """The 50's were swell."""
        errors = dates.check_decade_apostrophes_short(text)
        assert len(errors) == 1

        text = """From 1999-2002, Sally served as chair of the committee."""
        errors = dates.check_dash_and_from(text)
        print(errors)
        assert len(errors) == 1
