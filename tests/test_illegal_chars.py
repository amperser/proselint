"""Check that the CLI can handle invalid characters."""

from .check import Check
from click.testing import CliRunner
from os.path import dirname, abspath, join
from proselint.command_line import proselint


class TestInvalidCharacters(Check):
    """Test class for testing invalid characters on the CLI"""

    __test__ = True

    def test_invalid_characters(self):
        """Ensure that a file with illegal characters does not break us."""
        curr_dir = dirname(abspath(__file__))
        test_file = join(curr_dir, "illegal-chars.txt")
        runner = CliRunner()

        output = runner.invoke(proselint, test_file)

        assert "UnicodeDecodeError" not in output.stdout
        assert "FileNotFoundError" not in output.stdout
