"""Tests for misc.false_plurals check."""

from proselint.checks.misc import false_plurals as chk

from .check import Check


class TestCheck(Check):
    """The test class for misc.false_plurals."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for misc.false_plurals."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""There were several phenomenons.""")

    def test_smoke_kudos(self):
        """Basic smoke test for misc.false_plurals.kudos."""
        assert chk.check_kudos("""Smoke phrase with nothing flagged.""") == []
        assert chk.check_kudos("""I give you many kudos.""") != []
