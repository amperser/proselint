"""Check that the --config command-line flag works"""

from proselint.tools import load_options


def test_load_options_function():
    overrides = load_options("tests/test_config_flag_proselintrc")
    assert load_options()["checks"]["uncomparables.misc"]
    assert not overrides["checks"]["uncomparables.misc"]
