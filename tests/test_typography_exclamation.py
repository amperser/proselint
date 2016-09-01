"""Tests for typography.exclamation check."""
from __future__ import absolute_import

from .check import Check

from proselint.checks.typography import exclamation as chk


class TestCheck(Check):
    """The test class for typography.exclamation."""

    __test__ = True

    @property
    def this_check(self):
        """Bolierplate."""
        return chk

    def test_smoke_repeated_exclamations(self):
        """Basic smoke test.

        Test for typography.exclamation.check_repeated_exclamations.
        """
        assert chk.check_repeated_exclamations(
            """Smoke phrase with nothing flagged.""") == []
        assert chk.check_repeated_exclamations(
            """I'm really excited!!""") != []

    def test_smoke_exclamations_ppm(self):
        """Basic smoke test.

        Test for typography.exclamation.check_exclamations_ppm.
        """
        assert chk.check_exclamations_ppm(
            """Smoke phrase with nothing flagged.""") == []
        assert chk.check_exclamations_ppm(
            """I'm really excited! Really!""") != []
