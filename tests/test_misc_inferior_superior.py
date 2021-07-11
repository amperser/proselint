"""Tests for misc.inferior_superior check."""

from proselint.checks.misc import inferior_superior as chk

from .check import Check


class TestCheck(Check):
    """The test class for misc.inferior_superior."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for misc.inferior_superior."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes(
            """It was more inferior than the alternative.""")
