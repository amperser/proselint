"""Tests for misc.metaconcepts check."""

from proselint.checks.misc import metaconcepts as chk

from .check import Check


class TestCheck(Check):
    """The test class for misc.metaconcepts."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for misc.metaconcepts."""
        pass
