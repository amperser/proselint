"""Test user option overrides using --config and load_options"""
import subprocess
from proselint.tools import deepmerge_dicts, load_options


def test_deepmerge_dicts():
    """Test deepmerge_dicts"""
    d1 = {'a': 1, 'b': {'c': 2, 'd': 3}}
    d2 = {'a': 2, 'b': {'c': 3, 'e': 4}}
    assert deepmerge_dicts(d1, d2) == {'a': 2, 'b': {'c': 3, 'd': 3, 'e': 4}}


def test_load_options_function():
    """Test load_options by specifying a user options path"""
    overrides = load_options("tests/test_config_flag_proselintrc")
    assert load_options()["checks"]["uncomparables.misc"]
    assert not overrides["checks"]["uncomparables.misc"]


def test_config_flag():
    """Test the --config CLI argument"""
    output = subprocess.run(["python", "-m", "proselint", "--demo"],
                            stdout=subprocess.PIPE, encoding='utf-8')
    assert "uncomparables.misc" in output.stdout

    output = subprocess.run(["python", "-m", "proselint", "--demo", "--config",
                             "tests/test_config_flag_proselintrc"],
                            stdout=subprocess.PIPE, encoding='utf-8')
    assert "uncomparables.misc" not in output.stdout

    output = subprocess.run(["python", "-m", "proselint", "--demo", "--config",
                             "non_existent_file"],
                            stderr=subprocess.PIPE, encoding='utf-8')
    assert output.returncode == 1
    assert "FileNotFoundError" in output.stderr
