"""Tests for misc.illogic check."""
from __future__ import absolute_import

from .check import Check

from proselint.checks.misc import illogic as chk


class TestCheck(Check):
    """The test class for misc.illogic."""

    __test__ = True

    @property
    def this_check(self):
        """Bolierplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for misc.illogic."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""We should preplan the trip.""")

    def test_smoke_coin_a_phrase_from(self):
        """Basic smoke test for misc.illogic.check_coin_a_phrase_from."""
        assert chk.check_coin_a_phrase_from(
            """Smoke phrase with nothing flagged.""") == []
        assert chk.check_coin_a_phrase_from(
            """To coin a phrase from him, No diggity""") != []

    def test_smoke_check_without_your_collusion(self):
        """Basic smoke test for misc.illogic."""
        assert chk.check_without_your_collusion(
            """Smoke phrase with nothing flagged.""") == []
        assert chk.check_without_your_collusion(
            """Not Without your collusion you won't'.""") != []
