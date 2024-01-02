"""Test user option overrides using --config and load_options"""
import json
from pathlib import Path

from click.testing import CliRunner

from proselint.command_line import proselint
from proselint.config_default import proselint_base
from proselint.tools import _deepmerge_dicts, load_options
from tests.conftest import print_invoke_return


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
    result = CliRunner().invoke(proselint, ["--demo"])
    print_invoke_return(result)
    assert "uncomparables.misc" in result.stdout


def test_config_flag_config():
    result = CliRunner().invoke(
        proselint,
        ["--demo", "--debug", "--config", "tests/test_config_flag_proselintrc.json"],
    )
    print_invoke_return(result)
    assert "uncomparables.misc" not in result.stdout


def test_config_flag_config_nonexist():
    result = CliRunner().invoke(proselint, ["--demo", "--config", "non_existent_file"])
    assert result.exit_code != 0
    assert result.exc_info[0].__name__ == "SystemExit"
    # was FileNotFoundError, but click is now doing pre-checks


def test_config_flag_data_nonexist():
    result = CliRunner().invoke(proselint, "non_existent_file")
    assert result.exit_code != 0
    assert result.exc_info[0].__name__ == "SystemExit"
    # was FileNotFoundError, but click is now doing pre-checks


def test_dump_config_default():
    """Test --dump-default-config and --dump-config"""
    result = CliRunner().invoke(proselint, "--dump-default-config")
    assert json.loads(result.stdout) == proselint_base


def test_dump_config():
    """this test is not optimal
    if triggered, the input-cfg was extended with the default-config
    -> add missing flags to input-cfg!
    """
    config_file = Path(__file__).parent / "test_config_flag_proselintrc.json"
    result = CliRunner().invoke(
        proselint,
        ["--dump-config", "--config", "tests/test_config_flag_proselintrc.json"],
    )
    assert json.loads(result.stdout) == json.load(config_file.open())
