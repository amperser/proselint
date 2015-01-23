import os
import subprocess


class TestSamples(object):

    def test_wpe(self):
        min_wpe = 50

        examples_dir = os.path.join(os.getcwd(), "tests", "samples")
        examples = os.listdir(examples_dir)

        for example in examples:
            example_path = os.path.join(examples_dir, example)
            out = subprocess.check_output(
                "proselint " + example_path,
                shell=True)

            # Compute the number of words per (wpe) error.
            num_errors = out.count("\n")

            with open(example_path, 'r') as f:
                text = f.read()
                num_words = len(text.split(' '))

            try:
                wpe = 1.0*num_words / num_errors
            except ZeroDivisionError:
                wpe = float('Inf')

            # Make sure that
            assert wpe > min_wpe, \
                "{} produced {} errors.".format(example, num_errors)
