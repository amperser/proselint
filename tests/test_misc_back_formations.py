"""Tests for misc.back_formations check."""

from proselint.checks.misc import back_formations as chk

from .check import Check


class TestCheck(Check):
    """The test class for misc.back_formations."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for misc.back_formations."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""It is an improprietous use.""")
