"""Test uncomparables.misc"""

from proselint.checks.uncomparables import misc as chk

from .check import Check


class TestCheck(Check):
    """The test class for uncomparables.misc."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for uncomparables.misc."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""The item was more unique.""")

    def test_sample_phrases(self):
        """Find 'very unique'."""
        assert not self.passes("""This sentence is very unique.""")

    def test_spaces(self):
        """Handle spacing correctly."""
        assert not self.passes("""This sentence is very\nunique.""")
        assert not self.passes("""Kind of complete.""")
        assert self.passes("""Every perfect instance.""")

    def test_constitutional(self):
        """Don't flag exceptions."""
        assert self.passes("""A more perfect union.""")
