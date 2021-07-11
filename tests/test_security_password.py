"""Tests for security.password check."""

from proselint.checks.security import password as chk

from .check import Check


class TestCheck(Check):
    """The test class for security.password."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for security.password."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""The password is 123456.""")
        assert not self.passes("""My password is PASSWORD.""")
