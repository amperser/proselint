"""Test garner.dates."""
from __future__ import absolute_import
from __future__ import print_function

from .check import Check
from proselint.checks.typography import exclamation


class TestCheck(Check):
    """Test class for leonard.exclamation."""

    __test__ = True

    def test_capitalization_and_no_exclamation(self):
        """Don't throw error when phrase has capitalization."""
        text = """
             The QUICK BROWN fox juMPED over the lazy cat.
        """
        errors = exclamation.check_repeated_exclamations(text)
        assert len(errors) == 0

    def test_exclamation(self):
        """Test leonard.exclamation. with exclamation marks."""
        text = """Sally sells seashells and they were too expensive!!!!"""
        errors = exclamation.check_repeated_exclamations(text)
        print(errors)
        assert len(errors) == 1
