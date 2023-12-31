"""Test user option overrides using --config and load_options"""
import json
import os
from pathlib import Path
from unittest.mock import patch

from click.testing import CliRunner

from proselint.command_line import proselint
from proselint.config import default
from proselint.tools import deepmerge_dicts, load_options

runner = CliRunner()


def test_deepmerge_dicts():
    """Test deepmerge_dicts"""
    d1 = {"a": 1, "b": {"c": 2, "d": 3}}
    d2 = {"a": 2, "b": {"c": 3, "e": 4}}
    assert deepmerge_dicts(d1, d2) == {"a": 2, "b": {"c": 3, "d": 3, "e": 4}}


@patch("os.path.isfile")
def test_load_options_function(isfile):
    """Test load_options by specifying a user options path"""

    isfile.side_effect = "tests/test_config_flag_proselintrc.json".__eq__

    config_file = Path(__file__).parent / "test_config_flag_proselintrc.json"
    overrides = load_options(config_file)
    assert load_options()["checks"]["uncomparables.misc"]
    assert not overrides["checks"]["uncomparables.misc"]

    isfile.side_effect = os.path.join(os.getcwd(), ".proselintrc.json").__eq__

    # TestCase().assertRaises(FileNotFoundError, load_options)
    # TODO: why does this test exist? messed up testing


def test_config_flag_demo():
    """Test the --config CLI argument"""
    output = runner.invoke(proselint, ["--demo"])
    assert "uncomparables.misc" in output.stdout


def test_config_flag_config():
    output = runner.invoke(
        proselint,
        ["--demo", "--config", "tests/test_config_flag_proselintrc.json"],
    )
    assert "uncomparables.misc" not in output.stdout


def test_config_flag_config_nonexist():
    output = runner.invoke(proselint, ["--demo", "--config", "non_existent_file"])
    assert output.exit_code != 0
    # assert output.exc_info[0].__name__ == "FileNotFoundError"


def test_config_flag_data_nonexist():
    output = runner.invoke(proselint, "non_existent_file")
    assert output.exit_code != 0
    # assert output.exc_info[0].__name__ == "FileNotFoundError"


def test_dump_config_default():
    """Test --dump-default-config and --dump-config"""
    output = runner.invoke(proselint, "--dump-default-config")
    assert json.loads(output.stdout) == default


def test_dump_config():
    config_file = Path(__file__).parent / "test_config_flag_proselintrc.json"
    output = runner.invoke(
        proselint,
        ["--dump-config", "--config", "tests/test_config_flag_proselintrc.json"],
    )
    assert json.loads(output.stdout) == json.load(config_file.open())
