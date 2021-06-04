"""Test the Cliches.misc module."""
from __future__ import absolute_import

from .check import Check

from proselint.checks.cliches import misc as chk


class TestCheck(Check):
    """The test class for cliches.misc."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_cliches(self):
        """Basic checks on check_cliches"""
        garner = """Worse than a fate worse than death."""
        write_good = """He's a chip off the old block."""
        gnu_diction = """It's a matter of concern."""

        assert self.passes("""No cliches here.""")
        for check in [garner, write_good, gnu_diction]:
            assert not self.passes(check)
