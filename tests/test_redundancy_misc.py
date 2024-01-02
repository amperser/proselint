"""Tests for redundancy.misc check."""

from proselint.checks.redundancy import misc
from tests.conftest import _fail, _pass


def test_smoke_check():
    """Basic smoke test for redundancy.misc.check."""
    check = misc.check
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _fail(check, "The table was rectangular in shape.")


def test_smoke_garner():
    """Basic smoke test for redundancy.misc.check_garner."""
    check = misc.check_garner
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _fail(check, "It was blatantly obvious what to do next.")


def test_smoke_nordquist():
    """Basic smoke test for redundancy.misc.check_norquist."""
    check = misc.check_nordquist
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _fail(check, "Taking the package was absolutely essential.")


def test_smoke_atd():
    """Basic smoke test for redundancy.misc.check_norquist."""
    check = misc.check_atd
    assert _pass(check, "Smoke phrase with nothing flagged.")
    assert _fail(check, "He often repeated the old adage.")
