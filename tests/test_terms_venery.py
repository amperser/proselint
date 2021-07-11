"""Tests for terms.venery check."""

from proselint.checks.terms import venery as chk

from .check import Check


class TestCheck(Check):
    """The test class for terms.venery."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for terms.venery."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""There was a group of alligators.""")
