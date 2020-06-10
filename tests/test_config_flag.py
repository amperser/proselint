"""Check that the --config command-line flag works"""

import subprocess


def test_default_config():
    """Ensure that linting the demo uses the default proselintrc with
    uncomparables.misc true"""
    output = subprocess.run(["python", "-m", "proselint", "--demo"],
                            stdout=subprocess.PIPE, encoding='utf-8')
    assert "uncomparables.misc" in output.stdout


def test_overriding_config():
    """Ensure that linting the demo and overriding uncomparables.misc to false
    has no such warnings"""
    output = subprocess.run(["python", "-m", "proselint", "--demo", "--config",
                             "tests/test_config_flag_proselintrc"],
                            stdout=subprocess.PIPE, encoding='utf-8')
    assert "uncomparables.misc" not in output.stdout
