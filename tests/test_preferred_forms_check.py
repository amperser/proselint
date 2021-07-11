"""Test the preferred_forms_check function from the tools.py module."""

from proselint.tools import preferred_forms_check as chk

from .check import Check


class TestCheck(Check):
    """The test class for tools.preferred_forms_check."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def setUp(self):
        """Create some test fixtures."""
        self.L = [['use', ['utilize']]]
        self.l_caps = [["Stone Age",  ["stone age"]]]
        self.err = 'error message'
        self.msg = 'use the preferred form'

    def test_smoke(self):
        """Basic smoke test for preferred_forms_check."""
        assert chk(
            "We utilize this tech", self.L, self.err, self.msg) != []
        assert chk(
            "We use this tech", self.L, self.err, self.msg) == []

    def test_capitalization(self):
        """Test for preferred forms involving capitalization."""
        assert not chk(
            "In the stone age", self.l_caps, self.err, self.msg,
            ignore_case=False)
        assert chk(
            "In the Stone Age", self.l_caps, self.err, self.msg,
            ignore_case=False) == []
