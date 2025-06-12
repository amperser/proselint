"""Tests for industrial_language.chatspeak check."""

from proselint.checks.industrial_language import chatspeak as chk

from .check import Check


class TestCheck(Check):
    """The test class for industrial_language.chatspeak."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for industrial_language.chatspeak."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""BRB getting coffee.""")
