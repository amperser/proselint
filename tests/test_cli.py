"""Verify that the CLI behaves correctly."""

import logging
from pathlib import Path

from pytest import LogCaptureFixture

from proselint.command_line import ExitStatus, get_parser, proselint
from proselint.version import __version__

CHAR_FILE = Path(__file__, "../invalid-chars.txt").resolve()
PARSER = get_parser()


def test_exit_code_demo() -> None:
    """Ensure that linting the demo returns an exit code of 1."""
    assert (
        proselint(
            PARSER.parse_args(
                (
                    "check",
                    "--demo",
                )
            ),
            PARSER,
        )
        == ExitStatus.SUCCESS_ERR
    )


def test_version(caplog: LogCaptureFixture) -> None:
    """Ensure that the version is logged and exits correctly."""
    with caplog.at_level("INFO", logger="proselint"):
        result = proselint(PARSER.parse_args(("version",)), PARSER)
        assert result == ExitStatus.SUCCESS
        assert caplog.record_tuples == [
            ("proselint", logging.INFO, f"Proselint {__version__}")
        ]


def test_invalid_characters() -> None:
    """Ensure that invalid characters do not break proselint."""
    assert (
        proselint(PARSER.parse_args(("check", CHAR_FILE.as_posix())), PARSER)
        == ExitStatus.SUCCESS
    )
