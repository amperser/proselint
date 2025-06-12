"""Tests for skunked_terms check."""

from proselint.checks import skunked_terms as chk

from .check import Check


class TestCheck(Check):
    """The test class for skunked_terms."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for skunked_terms."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes(
            """I gave an impassionate defence of the situation.""")
