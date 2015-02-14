"""Unit tests for strunk_white_eos."""

from check import Check
from proselint.checks import strunk_white_eos as chk


class TestCheck(Check):

    """Define the suite of checks."""

    def __init__(self):
        """Initialize the check."""
        self.this_check = chk

    __test__ = True

    def test_with_utilized(self):
        """Don't produce an error when 'use' is used correctly."""
        assert self.check(
            "I use a hammer to drive nails into wood."
        )

    def test_no_utilized(self):
        """Produce an error when 'utilize' is used in place of 'use'."""
        assert not self.check(
            "I utilize a hammer to drive nails into wood."
        )
