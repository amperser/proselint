"""Test the Cliches.misc module."""

from proselint.checks.cliches import misc
from tests.conftest import _fail, _pass


def test_cliches_garner_basic():
    """Basic checks on check_cliches_garner."""
    text = "Worse than a fate worse than death."
    check = misc.check_cliches_garner
    assert _pass(check, "No cliches here.")
    assert _fail(check, text)
    assert "cliches.garner" in check(text)[0]


def test_cliches_write_good_basic():
    """Basic checks on check_cliches_write_good."""
    text = "He's a chip off the old block."
    check = misc.check_cliches_write_good
    assert _pass(check, "No cliches here.")
    assert _fail(check, text)
    assert "cliches.write_good" in check(text)[0]


def test_cliches_gnu_diction_basic():
    """Basic check on check_cliches_gnu_diction."""
    text = "It's a matter of concern."
    check = misc.check_cliches_gnu_diction
    assert _pass(check, "No cliches here.")
    assert _fail(check, text)
    assert "cliches.gnu_diction" in check(text)[0]
