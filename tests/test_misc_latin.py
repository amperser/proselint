"""Tests for misc.latin check."""

from proselint.checks.misc import latin as chk

from .check import Check


class TestCheck(Check):
    """The test class for misc.latin."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for misc.latin."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""And ceteris paribus, it was good.""")
