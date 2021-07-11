"""Tests for hyperbole.misc check."""

from proselint.checks.hyperbole import misc as chk

from .check import Check


class TestCheck(Check):
    """The test class for hyperbole.misc."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for hyperbole.misc."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""So exaggerated!!!""")
