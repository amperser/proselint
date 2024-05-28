"""Test user option overrides using --config and load_options."""
import json
import logging
import sys
from pathlib import Path
from unittest.mock import patch

import pytest

from proselint.command_line import proselint
from proselint.config_base import proselint_base
from proselint.tools import _deepmerge_dicts, load_options

CONFIG_FILE = Path(__file__).parent / "test-proselintrc.json"


def test_deepmerge_dicts() -> None:
    """Test deepmerge_dicts."""
    d1 = {"a": 1, "b": {"c": 2, "d": 3}}
    d2 = {"a": 2, "b": {"c": 3, "e": 4}}
    assert _deepmerge_dicts(d1, d2) == {"a": 2, "b": {"c": 3, "d": 3, "e": 4}}


def test_load_options_function_default() -> None:
    """Test the default config of load_options."""
    assert load_options()["checks"]["uncomparables.misc"]


def test_load_options_function() -> None:
    """Test load_options by specifying a user options path."""
    default = load_options()
    assert default["checks"]["uncomparables.misc"]
    overrides = load_options(CONFIG_FILE)
    assert not overrides["checks"]["uncomparables.misc"]


def test_config_flag_demo(caplog: pytest.LogCaptureFixture) -> None:
    """Test the --config CLI argument."""
    test_args = ["proselint", "--demo", "-v"]
    with patch.object(sys, "argv", test_args), pytest.raises(
        SystemExit
    ) as exc_info, caplog.at_level(logging.INFO, "proselint"):
        proselint()
        assert "uncomparables.misc" in caplog.text
        assert "restricted.top1000" not in caplog.text
    assert int(str(exc_info.value)) >= 1


def test_config_flag_config(caplog: pytest.LogCaptureFixture) -> None:
    """Test the --config CLI argument."""
    test_args = [
        "proselint",
        "--demo",
        "-v",
        "--config",
        CONFIG_FILE.as_posix(),
    ]
    with patch.object(sys, "argv", test_args), pytest.raises(
        SystemExit
    ) as exc_info, caplog.at_level(logging.INFO, "proselint"):
        proselint()
        assert "uncomparables.misc" not in caplog.text
        assert "airlinese.misc" in caplog.text
    assert int(str(exc_info.value)) >= 1


def test_config_flag_config_nonexist() -> None:
    """Test the --config CLI argument."""
    test_args = ["proselint", "--demo", "--config", "non_existent_file"]
    with patch.object(sys, "argv", test_args), pytest.raises(
        FileNotFoundError
    ) as exc_info:
        proselint()
    assert "non_existent_file" in str(exc_info)


def test_config_flag_data_nonexist() -> None:
    """Test the --config CLI argument."""
    test_args = ["proselint", "non_existent_file"]
    with patch.object(sys, "argv", test_args), pytest.raises(
        FileNotFoundError
    ) as exc_info:
        proselint()
    assert "non_existent_file" in str(exc_info)


def test_dump_config_default(capsys: pytest.CaptureFixture) -> None:
    """Test dump-config subcommand with default config."""
    test_args = ["proselint", "dump-config", "--default"]
    with patch.object(sys, "argv", test_args), pytest.raises(
        SystemExit
    ) as exc_info:
        proselint()
    captured = capsys.readouterr()
    assert int(str(exc_info.value)) == 0
    assert json.loads(captured.err) == proselint_base


def test_dump_config(capsys: pytest.CaptureFixture) -> None:
    """
    Test dump-config subcommand with specified config.

    this is not optimal
    if triggered, the input-cfg was extended with the default-config
    -> add missing flags to input-cfg!
    """
    test_args = ["proselint", "dump-config", "--config", CONFIG_FILE.as_posix()]
    with patch.object(sys, "argv", test_args), pytest.raises(
        SystemExit
    ) as exc_info:
        proselint()
    captured = capsys.readouterr()
    assert int(str(exc_info.value)) == 0
    assert json.loads(captured.err) == json.load(CONFIG_FILE.open())
