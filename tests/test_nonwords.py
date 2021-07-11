"""Tests for nonwords.misc check."""

from proselint.checks.nonwords import misc as chk

from .check import Check


class TestCheck(Check):
    """The test class for nonwords.misc."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for nonwords.misc."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""The test was good irregardless.""")
