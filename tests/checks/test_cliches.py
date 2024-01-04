"""Test the Cliches.misc module."""

from proselint.checks.cliches import misc
from tests.conftest import assert_fail
from tests.conftest import assert_pass


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
    check = misc.check_cliches_write_good_a_to_c
    assert_pass(check, "No cliches here.")
    assert_fail(check, text)
    assert "cliches.write_good" in check(text)[0]


def test_write_good_c():
    """Basic checks on check_cliches_write_good."""
    check = misc.check_cliches_write_good_a_to_c
    assert_pass(check, "No cliches here.")
    assert_fail(check, "You sound like a broken record.")
    assert_fail(check, "You gave me a crash course in xyz.")


def test_write_good_g():
    """Basic checks on check_cliches_write_good."""
    check = misc.check_cliches_write_good_d_to_j
    assert_pass(check, "No cliches here.")
    assert_fail(check, "You always had a green thumb.")


def test_write_good_k():
    """Basic checks on check_cliches_write_good."""
    check = misc.check_cliches_write_good_k_to_o
    assert_pass(check, "No cliches here.")
    assert_fail(check, "You know the score.")
    assert_fail(check, "You payed out of pocket for years.")


def test_write_good_s():
    """Basic checks on check_cliches_write_good."""
    check = misc.check_cliches_write_good_p_to_s
    assert_pass(check, "No cliches here.")
    assert_fail(check, "I feel sick as a dog since yesterday.")
    assert_fail(check, "I feel sick as a dog.")


def test_write_good_t():
    """Basic checks on check_cliches_write_good."""
    check = misc.check_cliches_write_good_t_to_z
    assert_pass(check, "No cliches here.")
    assert_fail(check, "You, me and that uphill battle.")
    assert_fail(check, "You, me and that uphill battle with him.")


def test_gnu_diction():
    """Basic check on check_cliches_gnu_diction."""
    text = "It's a matter of concern."
    check = misc.check_cliches_gnu_diction
    assert_pass(check, "No cliches here.")
    assert_fail(check, text)
    assert "cliches.gnu_diction" in check(text)[0]
