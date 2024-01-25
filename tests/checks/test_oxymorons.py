"""Tests for oxymorons.misc check."""

from proselint.checks.oxymorons.misc import check
from tests.conftest import assert_fail
from tests.conftest import assert_pass


def test():
    """Basic smoke test for oxymorons.misc."""
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "He needed an exact estimate.")
