"""Tests for misc.but check."""

from proselint.checks.misc import but as chk

from .check import Check


class TestCheck(Check):
    """The test class for misc.but."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for misc.but."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""But I never start with the word "but".""")
        assert self.passes("""I never start with the word "but",
but might use it after a linebreak.""")
