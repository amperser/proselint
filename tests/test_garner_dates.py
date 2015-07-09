from check import Check
from proselint.checks.garner import dates


class TestCheck(Check):

    __test__ = True

    def test_50s_hyphenation(self):
        text = """The 50's were swell."""
        errors = dates.check_decade_apostrophes_short(text)
        assert len(errors) == 1

    def test_50_Cent_hyphenation(self):
        text = """Dr. Dre suggested to 50's manager that he look into signing
                  Eminem to the G-Unit record label."""
        errors = dates.check_decade_apostrophes_short(text)
        assert len(errors) == 0
