"""Test dfw.uncomparables."""

from check import Check
from proselint.checks.wallace import uncomparables as chk


class TestCheck(Check):

    """The test class for dfw.uncomparables."""

    __test__ = True

    @property
    def this_check(self):
        """Bolierplate."""
        return chk

    def test_sample_phrases(self):
        """Find 'very unique'."""
        assert not self.check("""This sentence is very unique.""")

    def test_linebreaks(self):
        """Handle linebreaks correctly."""
        assert not self.check("""This sentence is very\nunique.""")
