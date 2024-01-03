"""Test the Cliches.misc module."""

from proselint.checks.cliches import misc
from tests.conftest import assert_fail, assert_pass


def test_garner():
    """Basic checks on check_cliches_garner."""
    text = "Worse than a fate worse than death."
    check = misc.check_cliches_garner
    assert_pass(check, "No cliches here.")
    assert_fail(check, text)
    assert "cliches.garner" in check(text)[0]


def test_write_good():
    """Basic checks on check_cliches_write_good."""
    text = "He's a chip off the old block."
    check = misc.check_cliches_write_good_cdef
    assert_pass(check, "No cliches here.")
    assert_fail(check, text)
    assert "cliches.write_good" in check(text)[0]


def test_write_good_a():
    """Basic checks on check_cliches_write_good."""
    check = misc.check_cliches_write_good_ab
    assert_pass(check, "No cliches here.")
    assert_fail(check, "You sound like a broken record.")


def test_write_good_c():
    """Basic checks on check_cliches_write_good."""
    check = misc.check_cliches_write_good_cdef
    assert_pass(check, "No cliches here.")
    assert_fail(check, "You gave me a crash course in xyz.")


def test_write_good_g():
    """Basic checks on check_cliches_write_good."""
    check = misc.check_cliches_write_good_ghij
    assert_pass(check, "No cliches here.")
    assert_fail(check, "You always had a green thumb.")


def test_write_good_k():
    """Basic checks on check_cliches_write_good."""
    check = misc.check_cliches_write_good_klmn
    assert_pass(check, "No cliches here.")
    assert_fail(check, "You know the score.")


def test_write_good_o():
    """Basic checks on check_cliches_write_good."""
    check = misc.check_cliches_write_good_opqr
    assert_pass(check, "No cliches here.")
    assert_fail(check, "You payed out of pocket for years.")


def test_write_good_s():
    """Basic checks on check_cliches_write_good."""
    check = misc.check_cliches_write_good_opqr
    assert_pass(check, "No cliches here.")
    assert_fail(check, "I feel sick like a dog since yesterday.")
    assert_fail(check, "I feel sick like a dog.")


def test_write_good_u():
    """Basic checks on check_cliches_write_good."""
    check = misc.check_cliches_write_good_uvwxyz
    assert_pass(check, "No cliches here.")
    assert_fail(check, "You, me and that uphill battle.")


def test_gnu_diction():
    """Basic check on check_cliches_gnu_diction."""
    text = "It's a matter of concern."
    check = misc.check_cliches_gnu_diction
    assert_pass(check, "No cliches here.")
    assert_fail(check, text)
    assert "cliches.gnu_diction" in check(text)[0]
