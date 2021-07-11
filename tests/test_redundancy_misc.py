"""Tests for redundancy.misc check."""

from proselint.checks.redundancy import misc as chk

from .check import Check


class TestCheck(Check):
    """The test class for redundancy.misc."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_smoke_check(self):
        """Basic smoke test for redundancy.misc.check."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""The table was rectangular in shape.""")

    def test_smoke_garner(self):
        """Basic smoke test for redundancy.misc.check_garner."""
        assert chk.check_garner(
            """Smoke phrase with nothing flagged.""") == []
        assert chk.check_garner(
            """It was blatantly obvious what to do next.""") != []

    def test_smoke_nordquist(self):
        """Basic smoke test for redundancy.misc.check_norquist."""
        assert chk.check_nordquist(
            """Smoke phrase with nothing flagged.""") == []
        assert chk.check_nordquist(
            """Taking the package was absolutely essential.""") != []

    def test_smoke_atd(self):
        """Basic smoke test for redundancy.misc.check_norquist."""
        assert chk.check_atd(
            """Smoke phrase with nothing flagged.""") == []
        assert chk.check_atd(
            """He often repeated the old adage.""") != []
