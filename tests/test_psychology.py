"""Tests for psychology check."""

from proselint.checks import psychology as chk

from .check import Check


class TestCheck(Check):
    """The test class for psychology."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_smoke_lie_detector_test(self):
        """Basic smoke test for psychology.check_lie_detector_test."""
        assert chk.check_lie_detector_test(
            """Smoke phrase with nothing flagged.""") == []
        assert chk.check_lie_detector_test(
            """The defendant took a lie detector test.""") != []

    def test_smoke_p_equals_zero(self):
        """Basic smoke test for psychology.check_p_equals_zero."""
        assert chk.check_p_equals_zero(
            """Smoke phrase with nothing flagged.""") == []
        assert chk.check_p_equals_zero(
            """The effect was highly signficant at p = 0.00.""") != []

    def test_smoke_mental_telepathy(self):
        """Basic smoke test for psychology.check_mental_telepathy."""
        assert chk.check_mental_telepathy(
            """Smoke phrase with nothing flagged.""") == []
        assert chk.check_mental_telepathy(
            """I've been practicing mental telepathy.""") != []
