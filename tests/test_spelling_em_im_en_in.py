"""Tests for spelling.em_im_en_in check."""

from proselint.checks.spelling import em_im_en_in as chk

from .check import Check


class TestCheck(Check):
    """The test class for spelling.em_im_en_in."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for spelling.em_im_en_in."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""We shall imbark on a voyage.""")
