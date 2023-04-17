"""Tests for punctuation_spacing.misc check."""

from proselint.checks.punctuation_spacing import punctuation_spacing as chk

from .check import Check


class TestCheck(Check):
    """The test class for nonwords.misc."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_end_punctuation(self):
        """Tests end punctuation spacing."""
        test_phrase = """Smoke phrase with nothing flagged!"""
        assert chk.end_punctuation_spacing_check(test_phrase) == []

        test_phrase1 = """flagged!    """
        assert chk.end_punctuation_spacing_check(test_phrase1) != []

        test_phrase2 = """flagged?  """
        assert chk.end_punctuation_spacing_check(test_phrase2) == []

        test_phrase3 = """flagged?    """
        assert chk.end_punctuation_spacing_check(test_phrase3) != []

    def test_general_punctuation(self):
        """Tests general puncutation spacing."""
        test_phrase = """The quick brown fox jumps; over the lazy dog!"""
        assert chk.general_spacing_check(test_phrase) == []

        test_phrase1 = """The quick brown fox jumps;  over the lazy dog!"""
        assert chk.general_spacing_check(test_phrase1) != []

        test_phrase2 = """The quick brown fox jumps:over the lazy dog!"""
        assert chk.general_spacing_check(test_phrase2) == []

        test_phrase2 = """The quick brown fox jumps  :over the lazy dog!"""
        assert chk.general_spacing_check(test_phrase2) == []
