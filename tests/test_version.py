"""Test version number."""
from click.testing import CliRunner

from proselint.command_line import proselint
from proselint.version import __version__
from tests.conftest import print_invoke_return


def test_version():
    """Make sure the version number is correct."""
    result = CliRunner().invoke(proselint, "--version")

    print_invoke_return(result)
    assert __version__ in result.stdout
