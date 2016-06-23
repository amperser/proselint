"""Test junge.but."""
from __future__ import absolute_import
from __future__ import print_function

from .check import Check
from proselint.checks.misc import but

from nose.tools import assert_equals


class TestCheck(Check):
    """Test class for paragraph."""

    __test__ = True

    def test_starting_with_But_is_error(self):
        """Starting with but should be an error."""
        text = 'But I don\'t know what to say?'
        errors = but.check_dont_start_with_buts(text)
        assert_equals(len(errors), 1)

    def test_starting_with_lowercase_but_is_error(self):
        """Starting with lowercase but should be an error."""
        text = 'but I don\'t know what to say?'
        errors = but.check_dont_start_with_buts(text)
        assert_equals(len(errors), 1)

    def test_starts_with_valid_word(self):
        """Starting with a valid word is not an error."""
        text = 'Hello.'
        errors = but.check_dont_start_with_buts(text)
        assert_equals(len(errors), 0)

    def test_butcher_is_ok(self):
        """Butcher is not an error, even though it has a But."""
        text = 'Butchers are ok.'
        errors = but.check_dont_start_with_buts(text)
        assert_equals(len(errors), 0)

    def test_but_in_middle_of_paragraph(self):
        """But in the middle of a sentence is ok."""
        text = 'I\'ve got nothing but nice things to say.'
        errors = but.check_dont_start_with_buts(text)
        assert_equals(len(errors), 0)

    def test_but_after_a_newline(self):
        """But after a newline should be an error."""
        text = '\nBut what more.'
        errors = but.check_dont_start_with_buts(text)
        assert_equals(len(errors), 1)

    def test_but_after_a_newline_and_whitespace(self):
        """But after a newline and whitespace should be an error."""
        text = '\n But what more.'
        errors = but.check_dont_start_with_buts(text)
        assert_equals(len(errors), 1)
