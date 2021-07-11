"""Tests for misc.capitalization check."""

from proselint.checks.misc import capitalization as chk

from .check import Check


class TestCheck(Check):
    """The test class for misc.capitalization."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for misc.capitalization.check."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""It goes back to the stone age.""")

    def test_smoke_check_months(self):
        """Basic smoke test for misc.capitalization.check_months."""
        assert chk.check_months("""Smoke phrase with nothing flagged""") == []
        assert chk.check_months("""A nice day in june.""") != []

    def test_smoke_check_days(self):
        """Basic smoke test for misc.capitalization.check_days."""
        assert chk.check_days("""Smoke phrase with nothing flagged""") == []
        assert chk.check_days("""It happened on friday.""") != []
