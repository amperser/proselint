import os
import subprocess


class TestSamples(object):

    def test_samples(self):
        examples_dir = os.path.join(os.getcwd(), "tests", "samples")
        examples = os.listdir(examples_dir)

        for example in examples:
            example_path = os.path.join(examples_dir, example)
            out = subprocess.check_output(
                "proselint " + example_path,
                shell=True)

            num_errors = out.count("\n")

            assert num_errors == 0, \
                "{} produced {} errors.".format(example, num_errors)
