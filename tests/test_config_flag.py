"""Check that the --config command-line flag works"""

from proselint.tools import load_options


def test_load_options_function():
    overrides = load_options("tests/test_config_flag_proselintrc")
    assert load_options()["checks"]["uncomparables.misc"]
    assert not overrides["checks"]["uncomparables.misc"]


def test_load_fallbacks():
    fallbacks = load_options(None, ["tests/test_config_flag_proselintrc"])
    assert not fallbacks["checks"]["uncomparables.misc"]
    fallbacks = load_options(None, ["./.proselintrc"])
    assert fallbacks["checks"]["uncomparables.misc"]
