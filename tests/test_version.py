"""Test version number."""
import logging
import sys
from unittest.mock import patch

import pytest

from proselint.command_line import proselint
from proselint.version import __version__


def test_version(caplog: pytest.LogCaptureFixture) -> None:
    """Make sure the version number is correct."""
    test_args = ["proselint", "--version"]
    with patch.object(sys, "argv", test_args), pytest.raises(
        SystemExit
    ) as exc_info, caplog.at_level(logging.INFO, "proselint"):
        proselint()
        assert caplog.record_tuples == [
            ("proselint", logging.INFO, f"Proselint {__version__}")
        ]
    assert int(str(exc_info.value)) == 0
