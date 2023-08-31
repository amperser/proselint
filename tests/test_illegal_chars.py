"""Check that the CLI can handle invalid characters."""

from os.path import abspath, dirname, join

from click.testing import CliRunner

from proselint.command_line import proselint

from .check import Check


class TestInvalidCharacters(Check):
    """Test class for testing invalid characters on the CLI"""

    __test__ = True

    def test_invalid_characters(self):
<<<<<<< HEAD:tests/test_illegal_chars.py
        """Ensure that a file with illegal characters does not break us."""
        curr_dir = dirname(abspath(__file__))
        test_file = join(curr_dir, "illegal-chars.txt")
||||||| parent of 5d92d50... chore: lint:tests/test_invalid_chars.py
        """Ensure that a file with invalid characters does not break proselint."""
=======
        """Ensure that invalid characters do not break proselint."""
>>>>>>> 5d92d50... chore: lint:tests/test_invalid_chars.py
        runner = CliRunner()

        output = runner.invoke(proselint, test_file)

        assert "UnicodeDecodeError" not in output.stdout
        assert "FileNotFoundError" not in output.stdout
