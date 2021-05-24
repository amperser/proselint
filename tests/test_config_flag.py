"""Test user option overrides using --config and load_options"""
import subprocess
from proselint.tools import load_options


def test_load_options_function():
    """Test load_options by specifying a user options path"""
    overrides = load_options("tests/test_config_flag_proselintrc")
    assert load_options()["checks"]["uncomparables.misc"]
    assert not overrides["checks"]["uncomparables.misc"]


def test_load_fallbacks():
    """Test load_options with a fallback path"""
    fallbacks = load_options(None, ["tests/test_config_flag_proselintrc"])
    assert not fallbacks["checks"]["uncomparables.misc"]
    fallbacks = load_options(None, ["./.proselintrc"])
    assert fallbacks["checks"]["uncomparables.misc"]


def test_config_flag():
    """Test the --config CLI argument"""
    output = subprocess.run(["python", "-m", "proselint", "--demo"],
                            stdout=subprocess.PIPE, encoding='utf-8')
    assert "uncomparables.misc" in output.stdout
    output = subprocess.run(["python", "-m", "proselint", "--demo", "--config",
                             "tests/test_config_flag_proselintrc"],
                            stdout=subprocess.PIPE, encoding='utf-8')
    assert "uncomparables.misc" not in output.stdout
