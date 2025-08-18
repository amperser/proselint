"""Verify that the CLI behaves correctly."""

from pathlib import Path

from click.testing import CliRunner
from pytest import fixture

from proselint.command_line import proselint
from proselint.version import __version__

CHAR_FILE = Path(__file__, "../invalid-chars.txt").resolve()


@fixture
def _runner() -> CliRunner:  # pyright: ignore[reportUnusedFunction]
    return CliRunner()


def test_exit_code_demo(_runner: CliRunner) -> None:
    """Ensure that linting the demo returns an exit code of 1."""
    output = _runner.invoke(proselint, "--demo")
    assert output.exit_code == 1


def test_exit_code_version(_runner: CliRunner) -> None:
    """Ensure that getting the version returns an exit code of 0."""
    output = _runner.invoke(proselint, "--version")
    assert output.exit_code == 0


def test_invalid_characters(_runner: CliRunner) -> None:
    """Ensure that invalid characters do not break proselint."""
    runner = CliRunner()

    output = runner.invoke(proselint, CHAR_FILE.as_posix())

    assert "UnicodeDecodeError" not in output.stdout
    assert "FileNotFoundError" not in output.stdout


def test_version(_runner: CliRunner) -> None:
    """Ensure that the version number is correct."""
    runner = CliRunner()

    output = runner.invoke(proselint, "--version")
    assert __version__ in output.stdout
