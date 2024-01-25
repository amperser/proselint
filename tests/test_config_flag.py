"""Test user option overrides using --config and load_options"""
import json
from pathlib import Path
from unittest.mock import patch

from click.testing import CliRunner

from proselint.command_line import proselint
from proselint.config_base import proselint_base
from proselint.tools import _deepmerge_dicts  # noqa: PLC2701
from proselint.tools import load_options
from tests.conftest import print_invoke_return

CONFIG_FILE = Path(__file__, "../test-proselintrc.json").resolve()
FLAG = ["--config", str(CONFIG_FILE)]


def test_deepmerge_dicts():
    """Test deepmerge_dicts"""
    d1 = {"a": 1, "b": {"c": 2, "d": 3}}
    d2 = {"a": 2, "b": {"c": 3, "e": 4}}
    assert _deepmerge_dicts(d1, d2) == {"a": 2, "b": {"c": 3, "d": 3, "e": 4}}


@patch("os.path.isfile")
def test_load_options_function(isfile):
    """Test load_options by specifying a user options path"""
    isfile.side_effect = CONFIG_FILE.__eq__

    overrides = load_options(CONFIG_FILE)
    default = load_options()
    assert default == proselint_base
    assert default["checks"]["uncomparables.misc"]
    assert not overrides["checks"]["uncomparables.misc"]

    isfile.side_effect = (Path.cwd() / ".proselintrc.json").__eq__


def test_config_flag_demo():
    """Test the --config CLI argument"""
    result = CliRunner().invoke(proselint, ["--demo", "-v"])
    print_invoke_return(result)
    assert "uncomparables.misc" in result.stdout


def test_config_flag_config():
    result = CliRunner().invoke(proselint, ["--demo", "-v", *FLAG])
    print_invoke_return(result)
    assert "uncomparables.misc" not in result.stdout


def test_config_flag_config_nonexist():
    result = CliRunner().invoke(
        proselint, ["--demo", "--config", "non_existent_file"]
    )
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
    output = CliRunner().invoke(proselint, ["--dump-config", *FLAG])
    assert json.loads(output.stdout) == json.load(CONFIG_FILE.open())
