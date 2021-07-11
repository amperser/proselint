"""Tests for spelling.misc check."""

from proselint.checks.spelling import misc as chk

from .check import Check


class TestCheck(Check):
    """The test class for spelling.misc."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for spelling.misc."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""I like this alot.""")
