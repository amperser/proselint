"""Tests for psychology.misc check."""
from __future__ import absolute_import

from .check import Check

from proselint.checks.psychology import misc as chk


class TestCheck(Check):
    """The test class for psychology.misc."""

    __test__ = True

    @property
    def this_check(self):
        """Bolierplate."""
        return chk

    def test_smoke_lie_detector_test(self):
        """Basic smoke test for psychology.misc.check_lie_detector_test."""
        assert chk.check_lie_detector_test(
            """Smoke phrase with nothing flagged.""") == []
        assert chk.check_lie_detector_test(
            """The defendant took a lie detector test.""") != []

    def test_smoke_p_equals_zero(self):
        """Basic smoke test for psychology.misc.check_p_equals_zero."""
        assert chk.check_p_equals_zero(
            """Smoke phrase with nothing flagged.""") == []
        assert chk.check_p_equals_zero(
            """The effect was highly signficant at p = 0.00.""") != []

    def test_smoke_mental_telepathy(self):
        """Basic smoke test for psychology.misc.check_mental_telepathy."""
        assert chk.check_mental_telepathy(
            """Smoke phrase with nothing flagged.""") == []
        assert chk.check_mental_telepathy(
            """I've been practicing mental telepathy.""") != []
