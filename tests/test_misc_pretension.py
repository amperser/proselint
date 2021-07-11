"""Tests for misc.pretension check."""

from proselint.checks.misc import pretension as chk

from .check import Check


class TestCheck(Check):
    """The test class for misc.pretension."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for misc.pretension."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""We need to reconceptualize the project.""")
