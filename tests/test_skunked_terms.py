"""Tests for skunked_terms.misc check."""

from proselint.checks.skunked_terms import misc as chk

from .check import Check


class TestCheck(Check):
    """The test class for skunked_terms.misc."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for skunked_terms.misc."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes(
            """I gave an impassionate defence of the situation.""")
