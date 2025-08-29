"""Verify that the CLI behaves correctly."""

import logging

from pytest import LogCaptureFixture

from proselint.command_line import ExitStatus, get_parser, proselint
from proselint.version import __version__

PARSER = get_parser()


def test_exit_code_demo() -> None:
    """Ensure that linting the demo returns an exit code of 1."""
    assert (
        proselint(PARSER.parse_args(("check", "--demo")), PARSER)
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
