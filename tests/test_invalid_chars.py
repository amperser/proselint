"""Check that the CLI can handle invalid characters."""

from pathlib import Path

from click.testing import CliRunner

from proselint.command_line import proselint
from tests.conftest import print_invoke_return


CHAR_FILE = Path(__file__, "../invalid-chars.txt").resolve()

def test_invalid_characters():
    """Ensure that invalid characters do not break proselint."""
    runner = CliRunner()

    result = runner.invoke(proselint, CHAR_FILE.as_posix())
    print_invoke_return(result)

    assert result.exit_code == 0
    assert "UnicodeDecodeError" not in result.stdout
    assert "FileNotFoundError" not in result.stdout
