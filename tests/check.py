from unittest import TestCase
import os


class Check(TestCase):

    __test__ = False

    @property
    def this_check(self):
        raise NotImplementedError

    def check(self, lst):
        if isinstance(lst, basestring):
            lst = [lst]

        errors = []
        for text in lst:
            errors.append(self.this_check.check(text))

        return len(errors[0]) == 0

    def test_wpe(self):
        min_wpe = 50

        examples_dir = os.path.join(os.getcwd(), "tests", "samples")
        examples = os.listdir(examples_dir)

        for example in examples:
            example_path = os.path.join(examples_dir, example)

            # Compute the number of words per (wpe) error.
            with open(example_path, 'r') as f:
                text = f.read()
                num_errors = len(self.this_check.check(text))
                num_words = len(text.split(' '))

            try:
                wpe = 1.0*num_words / num_errors
            except ZeroDivisionError:
                wpe = float('Inf')

            # Make sure that
            assert wpe > min_wpe, \
                "{} has only {} wpe.".format(example, round(wpe, 2))
