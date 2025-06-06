"""Tests for nonwords check."""

from proselint.checks import nonwords as chk

from .check import Check


class TestCheck(Check):
    """The test class for nonwords."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for nonwords."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""The test was good irregardless.""")
