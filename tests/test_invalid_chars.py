"""Check that the CLI can handle invalid characters."""

from pathlib import Path

from click.testing import CliRunner

from proselint.command_line import proselint

from .check import Check

CHAR_FILE = Path(__file__, "../invalid-chars.txt").resolve()


class TestInvalidCharacters(Check):
    """Test class for testing invalid characters on the CLI"""

    __test__ = True

    def test_invalid_characters(self):
        """Ensure that invalid characters do not break proselint."""
        runner = CliRunner()

        output = runner.invoke(proselint, CHAR_FILE)

        assert "UnicodeDecodeError" not in output.stdout
        assert "FileNotFoundError" not in output.stdout
