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
        assert len(chk.check_misplaced("""See Smith et. al.""")) == 1

        assert (
            len(
                chk.check_spacing(
                    """This is good. Only one space each time. Every time."""
                )
            )
            == 0
        )
        assert (
            len(chk.check_spacing("""This is bad.  Not consistent. At all."""))
            == 1
        )

        assert len(chk.check_hyperbole("""So exaggerated!!!""")) == 1

    def test_smoke_exclamations_ppm(self):
        """
        Basic smoke test.

        Test for typography.punctuation.exclamation
        """
        assert (
            chk.check_exclamations_ppm("""Smoke phrase with nothing flagged.""")
            == []
        )
        assert (
            chk.check_exclamations_ppm("""I'm really excited! Really!""") != []
        )
