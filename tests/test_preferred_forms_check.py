"""Test the preferred_forms_check function from the tools.py module."""
from __future__ import absolute_import

from .check import Check

from proselint.tools import preferred_forms_check as chk

from nose import SkipTest


class TestCheck(Check):
    """The test class for tools.preferred_forms_check."""

    __test__ = True

    @property
    def this_check(self):
        """Bolierplate."""
        return chk

    def setUp(self):
        """Create some test fixtures."""
        self.l = [['use', ['utilize']]]
        self.l_caps = [['Canada', ['canada']]]
        self.err = 'error message'
        self.msg = 'use the preferred form'

    def test_smoke(self):
        """Basic smoke test for preferred_forms_check."""
        raise SkipTest
        assert chk(
            """We utilize this tech""", self.l, self.err, self.msg) != []
        assert chk(
            """We use this tech""", self.l, self.err, self.msg) == []

    def test_capitalization(self):
        """Test for preferred forms involving capitalization."""
        raise SkipTest
        assert chk(
            """"I live in canada""", self.l_caps, self.err, self.msg) != []
        assert chk(
            """"I live in Canada""", self.l_caps, self.err, self.msg) == []
