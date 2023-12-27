"""Check that the CLI can handle invalid characters."""

from pathlib import Path

from click.testing import CliRunner

from proselint.command_line import proselint

from .check import Check


class TestInvalidCharacters(Check):
    """Test class for testing invalid characters on the CLI"""

    __test__ = True

    def test_invalid_characters(self):
        """Ensure that a file with illegal characters does not break us."""
        test_path = Path(__file__).parent
        test_file = test_path / "illegal-chars.txt"
        runner = CliRunner()

        output = runner.invoke(proselint, test_file)

        assert "UnicodeDecodeError" not in output.stdout
        assert "FileNotFoundError" not in output.stdout
