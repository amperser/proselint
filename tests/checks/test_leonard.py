"""Test garner.dates."""
from proselint.checks.typography import exclamation
from tests.conftest import assert_fail, assert_pass


def test_repeated_exclamations():
    """Test leonard.exclamation. with exclamation marks."""
    check = exclamation.check_repeated_exclamations
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_pass(check, "The QUICK BROWN fox juMPED over the lazy cat.")
    assert_fail(check, "Sally sells seashells and they were too expensive!!!!")


def test_exclamation_ppm():
    check = exclamation.check_exclamations_ppm
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_pass(check, "Sally sells seashells and they were too expensive!")
    assert_fail(
        check,
        "Sally sells seashells and they were too expensive! They were not!",
    )
