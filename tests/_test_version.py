"""Test version number."""
from click.testing import CliRunner

from proselint.command_line import proselint
from proselint.version import __version__

from .check import Check


class TestCheck(Check):
    """Test class for version number."""

    __test__ = True

    def test_version(self):
        """Make sure the version number is correct."""
        runner = CliRunner()

        output = runner.invoke(proselint, "--version")
        assert __version__ in output.stdout
