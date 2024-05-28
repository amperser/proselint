"""Check that the CLI can handle invalid characters."""
import sys
from unittest.mock import patch
from pathlib import Path

import pytest

from proselint.command_line import proselint

CHAR_FILE = Path(__file__, "../invalid-chars.txt").resolve()


def test_invalid_characters(capsys: pytest.CaptureFixture):
    """Ensure that invalid characters do not break proselint."""
    test_args = ["proselint", CHAR_FILE.as_posix()]
    with patch.object(sys, "argv", test_args), pytest.raises(
        SystemExit
    ) as exc_info:
        proselint()
    assert int(str(exc_info.value)) == 0
    captured = capsys.readouterr()
    assert "UnicodeDecodeError" not in captured.err
    assert "FileNotFoundError" not in captured.err
