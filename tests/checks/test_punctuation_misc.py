"""Tests for punctuation.misc check."""

from proselint.checks.punctuation.misc import check_garner as check
from tests.conftest import assert_fail
from tests.conftest import assert_pass

# TODO: there is more than garner now

def test():
    """Basic smoke test for punctuation.misc.garner."""
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "See Smith et. al.")
