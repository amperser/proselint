"""Test user option overrides using --config and load_options"""
import json
from pathlib import Path
from unittest import TestCase
from unittest.mock import patch

from click.testing import CliRunner

from proselint.command_line import proselint
from proselint.config import DEFAULT, _deepmerge_dicts, load_from

runner = CliRunner()

CONFIG_FILE = Path(__file__).parent / "test-proselintrc.json"
FLAG = f"--config '{CONFIG_FILE}'"


def test_deepmerge_dicts():
    """Test deepmerge_dicts"""
    d1 = {"a": 1, "b": {"c": 2, "d": 3}, "f": 4, "g": 5}
    d2 = {"a": 2, "b": {"c": 3, "e": 4}, "g": {"h": 5}, "i": 6}
    assert _deepmerge_dicts(d1, d2) == {
        "a": 2,
        "b": {"c": 3, "d": 3, "e": 4},
        "f": 4,
        "g": {"h": 5},
        "i": 6,
    }

def test_load_from():
    """Test load_options by specifying a user options path"""

    overrides = load_from(CONFIG_FILE)
    assert load_from()["checks"]["uncomparables"]
    assert not overrides["checks"]["uncomparables"]


def test_config_flag():
    """Test the --config CLI argument"""
    output = runner.invoke(proselint, "--demo")
    assert "uncomparables" in output.stdout

    output = runner.invoke(proselint, f"--demo {FLAG}")
    assert "uncomparables" not in output.stdout
    assert "FileNotFoundError" != output.exc_info[0].__name__

    output = runner.invoke(proselint, "--demo --config non_existent_file")
    assert output.exit_code == 2

    output = runner.invoke(proselint, "non_existent_file")
    assert output.exit_code == 2


def test_dump_config():
    """Test --dump-default-config and --dump-config"""
    output = runner.invoke(proselint, "--dump-default-config")
    assert json.loads(output.stdout) == DEFAULT

    output = runner.invoke(proselint, f"--dump-config {FLAG}")
    assert json.loads(output.stdout) == json.loads(CONFIG_FILE.read_text())
