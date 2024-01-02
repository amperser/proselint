"""Test garner.dates."""
from proselint.checks.typography import exclamation
from tests.conftest import _pass, _fail


def test_capitalization_and_no_exclamation():
    """Don't throw error when phrase has capitalization."""
    text = "The QUICK BROWN fox juMPED over the lazy cat."
    check = exclamation.check_repeated_exclamations
    assert _pass(check, text)


def test_exclamation():
    """Test leonard.exclamation. with exclamation marks."""
    text = "Sally sells seashells and they were too expensive!!!!"
    check = exclamation.check_repeated_exclamations
    assert _fail(check, text)
