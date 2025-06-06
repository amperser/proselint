"""Tests for typography.punctuation check."""

from proselint.checks.typography import punctuation as chk

from .check import Check


class TestCheck(Check):
    """The test class for typography.punctuation."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for typography.punctuation."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""See Smith et. al.""")

        assert self.passes(
            """This is good. Only one space each time. Every time.""")
        assert not self.passes("""This is bad.  Not consistent. At all.""")

        assert not self.passes("""So exaggerated!!!""")


    def test_smoke_exclamations_ppm(self):
        """
        Basic smoke test.

        Test for typography.punctuation.exclamation
        """
        assert chk.check_exclamations_ppm(
            """Smoke phrase with nothing flagged.""") == []
        assert chk.check_exclamations_ppm(
            """I'm really excited! Really!""") != []
