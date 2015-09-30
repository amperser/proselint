"""Test version number."""
from __future__ import absolute_import
from __future__ import print_function

from .check import Check
from proselint.version import __version__
import subprocess


class TestCheck(Check):

    """Test class for version number."""

    __test__ = True

    def test_version(self):
        """Make sure the version number is correct."""
        out = subprocess.check_output("proselint --version", shell=True)
        assert out.decode('utf-8') == __version__ + "\n"
