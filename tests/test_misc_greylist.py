"""Tests for misc.greylist check."""

from proselint.checks.misc import greylist as chk

from .check import Check


class TestCheck(Check):
    """The test class for misc.greylist."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for misc.greylist."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""She should utilize her knowledge.""")
