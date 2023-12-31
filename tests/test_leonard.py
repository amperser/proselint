"""Test garner.dates."""
from proselint import log
from proselint.checks.typography import exclamation

from .check import Check


class TestCheck(Check):
    """Test class for leonard.exclamation."""

    __test__ = True

    def test_capitalization_and_no_exclamation(self):
        """Don't throw error when phrase has capitalization."""
        text = """
             The QUICK BROWN fox juMPED over the lazy cat.
        """
        results = exclamation.check_repeated_exclamations(text)
        assert len(results) == 0

    def test_exclamation(self):
        """Test leonard.exclamation. with exclamation marks."""
        text = """Sally sells seashells and they were too expensive!!!!"""
        results = exclamation.check_repeated_exclamations(text)
        log.info(results)
        assert len(results) == 1
