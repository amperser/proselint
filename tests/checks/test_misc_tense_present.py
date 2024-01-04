"""Tests for misc.tense_present check."""

from proselint.checks.misc.tense_present import check
from tests.conftest import assert_fail
from tests.conftest import assert_pass


def test():
    """Basic smoke test for misc.tense_present."""
    assert_pass(check, "Smoke phrase with nothing flagged.")

    assert_pass(check, "I did it by accident honestly.")
    assert_fail(check, "I did it on accident honestly.")
    assert_fail(check, "I did it On accident honestly.")

    assert_fail(check, "Told you something between you and i.")
    assert_fail(check, "Told you something between you and I.")

    assert_fail(check, "I feel nauseous.")
