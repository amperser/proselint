"""Check that the CLI returns the appropriate exit code."""

from click.testing import CliRunner

from proselint.command_line import proselint


def test_exit_code_demo():
    """Ensure that linting the demo returns an exit code of 1."""
    result = CliRunner().invoke(proselint, "--demo")
    assert result.exit_code >= 1


def test_exit_code_version():
    """Ensure that getting the version returns an exit code of 0."""
    result = CliRunner().invoke(proselint, "--version")
    assert result.exit_code == 0
