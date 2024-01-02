"""Check that the CLI can handle invalid characters."""

from pathlib import Path

from click.testing import CliRunner

from proselint.command_line import proselint


def test_invalid_characters():  # todo: probably broken
    """Ensure that a file with illegal characters does not break us."""
    test_path = Path(__file__).parent
    test_file = test_path / "illegal_chars.txt"
    result = CliRunner().invoke(proselint, test_file.as_posix())

    assert result.exit_code == 0
    assert "UnicodeDecodeError" not in result.stdout
    assert "FileNotFoundError" not in result.stdout
