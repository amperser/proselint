"""Test user option overrides using --config and load_options"""
import json
from pathlib import Path

from click.testing import CliRunner

from proselint.command_line import proselint
from proselint.config_default import default
from proselint.tools import _deepmerge_dicts, load_options

runner = CliRunner()


def test_deepmerge_dicts():
    """Test deepmerge_dicts"""
    d1 = {"a": 1, "b": {"c": 2, "d": 3}}
    d2 = {"a": 2, "b": {"c": 3, "e": 4}}
    assert _deepmerge_dicts(d1, d2) == {"a": 2, "b": {"c": 3, "d": 3, "e": 4}}


def test_load_options_function_default():
    assert load_options()["checks"]["uncomparables.misc"]


def test_load_options_function():
    """Test load_options by specifying a user options path"""
    config_file = Path(__file__).parent / "test_config_flag_proselintrc.json"
    overrides = load_options(config_file)
    assert not overrides["checks"]["uncomparables.misc"]


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
