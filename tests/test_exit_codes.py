"""Check that the CLI returns the appropriate exit code."""

import sys
from unittest.mock import patch

import pytest

from proselint.command_line import proselint


def test_exit_code_demo() -> None:
    """Ensure that linting the demo returns an exit code greater than 1."""
    test_args = ["proselint", "--demo"]
    with patch.object(sys, "argv", test_args), pytest.raises(
        SystemExit
    ) as excinfo:
        proselint()
    assert int(str(excinfo.value)) >= 1


def test_exit_code_version() -> None:
    """Ensure that getting the version returns an exit code of 0."""
    test_args = ["proselint", "--version"]
    with patch.object(sys, "argv", test_args), pytest.raises(
        SystemExit
    ) as excinfo:
        proselint()
    assert int(str(excinfo.value)) == 0
