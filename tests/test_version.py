"""Test version number."""
from click.testing import CliRunner

from proselint.command_line import proselint
from proselint.version import __version__


def test_version():
    """Make sure the version number is correct."""
    runner = CliRunner()

    output = runner.invoke(proselint, "--version")
    assert __version__ in output.stdout
