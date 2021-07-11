"""Tests for misc.composition check."""

from proselint.checks.misc import composition as chk

from .check import Check


class TestCheck(Check):
    """The test class for misc.composition."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for misc.composition."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""His story is not honest.""")
