"""Check that a check is working."""

import os
from pathlib import Path
from typing import Union
from unittest import TestCase


class Check(TestCase):
    """All tests inherit from Check."""

    __test__ = False

    def setUp(self):
        """Create a placeholder for setup procedure."""
        pass

    def tearDown(self):
        """Create a placeholder for teardown procedure."""
        pass

    @property
    def this_check(self):
        """Create a placeholder for the specific check."""
        raise NotImplementedError

    def passes(self, lst: Union[list, str]) -> bool:
        """Check if the test runs cleanly on the given text."""
        if isinstance(lst, str):
            lst = [lst]

        results = []
        for text in lst:
            results += self.this_check.check.__wrapped__(text)

        return len(results) == 0

    def wpe_too_high(self) -> None:
        """Check whether the check is too noisy."""
        min_wpe = 50

        examples_path = Path.cwd() / "tests" / "corpus"  # TODO: probably old path to corpus
        examples = os.listdir(examples_path)

        for example in examples:
            example_path = examples_path / example

            if ".DS_Store" in example_path:
                break

            # Compute the number of words per (wpe) error.
            with example_path.open(encoding='utf-8') as fh:
                text = fh.read()
                num_errors = len(self.this_check.check.__wrapped__(text))
                num_words = len(text)

            try:
                wpe = 1.0 * num_words / num_errors
            except ZeroDivisionError:
                wpe = float('Inf')

            # Make sure that
            assert wpe > min_wpe, \
                f"{example} has only {round(wpe, 2)} wpe."
