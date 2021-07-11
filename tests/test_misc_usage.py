"""Tests for misc.usage check."""

from proselint.checks.misc import usage as chk

from .check import Check


class TestCheck(Check):
    """The test class for misc.usage."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for misc.usage."""
        pass
