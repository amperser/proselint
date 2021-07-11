"""Tests for mixed_metaphors.misc check."""

from proselint.checks.mixed_metaphors import misc as chk

from .check import Check


class TestCheck(Check):
    """The test class for mixed_metaphors.misc."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_smoke_bottleneck(self):
        """Basic smoke test for check_bottleneck."""
        assert chk.check_bottleneck(
            """Smoke phrase with nothing flagged.""") == []
        assert chk.check_bottleneck(
            """The project produced a huge bottleneck.""") != []

    def test_smoke_misc(self):
        """Basic smoke test for check_misc."""
        assert chk.check_misc(
            """Smoke phrase with nothing flagged.""") == []
        assert chk.check_misc(
            """Writing tests is not rocket surgery.""") != []
