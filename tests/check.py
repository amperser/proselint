"""Check that a check is working."""

from unittest import TestCase
import os
from textblob import TextBlob
import codecs


class Check(TestCase):

    """All tests inherit from Check."""

    __test__ = False

    @property
    def this_check(self):
        """The specific check."""
        raise NotImplementedError

    def check(self, lst):
        """Check if the test runs cleanly on the given text."""
        if isinstance(lst, basestring):
            lst = [lst]

        errors = []
        for text in lst:
            blob = TextBlob(text)
            errors.append(self.this_check.check(blob))

        return len(errors[0]) == 0

    def test_wpe(self):
        """Check whether the check is too noisy."""
        min_wpe = 50

        examples_dir = os.path.join(os.getcwd(), "tests", "corpus")
        examples = os.listdir(examples_dir)

        for example in examples:
            example_path = os.path.join(examples_dir, example)

            # Compute the number of words per (wpe) error.
            with codecs.open(example_path, "r", encoding='utf-8') as f:
                blob = TextBlob(f.read())
                num_errors = len(self.this_check.check(blob))
                num_words = len(blob.words)

            try:
                wpe = 1.0 * num_words / num_errors
            except ZeroDivisionError:
                wpe = float('Inf')

            # Make sure that
            assert wpe > min_wpe, \
                "{} has only {} wpe.".format(example, round(wpe, 2))
