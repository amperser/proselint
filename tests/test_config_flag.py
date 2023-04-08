"""Test user option overrides using --config and load_options"""
import json
import os
from unittest import TestCase
from unittest.mock import patch

from click.testing import CliRunner

from proselint.command_line import proselint
from proselint.config import default
from proselint.tools import deepmerge_dicts, load_options

runner = CliRunner()


def test_deepmerge_dicts():
    """Test deepmerge_dicts"""
    d1 = {'a': 1, 'b': {'c': 2, 'd': 3}}
    d2 = {'a': 2, 'b': {'c': 3, 'e': 4}}
    assert deepmerge_dicts(d1, d2) == {'a': 2, 'b': {'c': 3, 'd': 3, 'e': 4}}


@patch("os.path.isfile")
def test_load_options_function(isfile):
    """Test load_options by specifying a user options path"""

    isfile.side_effect = "tests/test_config_flag_proselintrc.json".__eq__

    overrides = load_options("tests/test_config_flag_proselintrc.json", default)
    assert load_options(conf_default=default)["checks"]["uncomparables.misc"]
    assert not overrides["checks"]["uncomparables.misc"]

    isfile.side_effect = os.path.join(os.getcwd(), ".proselintrc.json").__eq__

    TestCase().assertRaises(FileNotFoundError, load_options)


def test_config_flag():
    """Test the --config CLI argument"""
    output = runner.invoke(proselint, "--demo")
    assert "uncomparables.misc" in output.stdout

    output = runner.invoke(
        proselint, "--demo --config tests/test_config_flag_proselintrc.json")
    assert "uncomparables.misc" not in output.stdout

    output = runner.invoke(proselint, "--demo --config non_existent_file")
    assert output.exit_code == 1
    assert "FileNotFoundError" == output.exc_info[0].__name__

    output = runner.invoke(proselint, "non_existent_file")
    assert output.exit_code == 2


def test_dump_config():
    """Test --dump-default-config and --dump-config"""
    output = runner.invoke(proselint, "--dump-default-config")
    assert json.loads(output.stdout) == default

    output = runner.invoke(
        proselint, "--dump-config --config tests/test_config_flag_proselintrc.json")
    assert json.loads(output.stdout) == json.load(
        open("tests/test_config_flag_proselintrc.json"))
