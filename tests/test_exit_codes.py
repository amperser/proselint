"""Check that the CLI returns the appropriate exit code."""

from click.testing import CliRunner

from proselint.command_line import proselint

from .check import Check


class TestExitCodes(Check):
    """Test class for CLI exit codes"""

    __test__ = True

    def setUp(self):
        self.runner = CliRunner()

    def test_exit_code_demo(self):
        """Ensure that linting the demo returns an exit code of 1."""
        output = self.runner.invoke(proselint, "--demo")
        assert output.exit_code == 1

    def test_exit_code_version(self):
        """Ensure that getting the version returns an exit code of 0."""
        output = self.runner.invoke(proselint, "--version")
        assert output.exit_code == 0
