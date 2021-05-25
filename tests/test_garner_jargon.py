"""Tests for garner.jargon check."""
from __future__ import absolute_import

from proselint.checks.garner import jargon as chk

from .check import Check


class TestCheck(Check):
    """The test class for garner.jargon."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    @property
    def test_smoke(self):
        """Basic smoke test for garner.jargon."""
        assert self.passes("""This sentence contains no jargon.""")
        assert not self.passes("""Whereas this conclusory sentence contains
        jargon.""")
