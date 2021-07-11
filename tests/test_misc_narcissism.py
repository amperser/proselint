"""Tests for misc.narcissism check."""

from proselint.checks.misc import narcissism as chk

from .check import Check


class TestCheck(Check):
    """The test class for misc.narcissism."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for misc.narcissism."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes(
            """In recent years, an increasing number of scientists have studied
             the problem in detail.""")
